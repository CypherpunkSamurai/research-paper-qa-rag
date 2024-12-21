import os, re
import httpx
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def parse_paper_id(paper_url: str) -> str:
    """
    Parse arXiv paper ID from URL
    Args:
        paper_url: URL string containing arXiv paper ID
    Returns:
        str: Paper ID
    Raises:
        ValueError: If URL format is invalid
    """
    pattern = r"arxiv\.org\/(?:abs|pdf)\/([0-9]+\.[0-9]+)(?:v\d+)?(?:\.pdf)?"
    match = re.search(pattern, paper_url.lower())
    
    if not match:
        raise ValueError("Invalid arXiv URL format")
        
    return match.group(1)

def download_paper(paper_url: str, filename: str):
    """
    Download Research Paper PDF
    """
    # parse paper id
    paper_id = parse_paper_id(paper_url)
    
    # get paper url
    paper_pdf_url = f"https://arxiv.org/pdf/{paper_id}.pdf"

    # get basefolder and make directory if not exists
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))

    # download the pdf
    try:
        with httpx.stream("GET", paper_pdf_url, follow_redirects=True) as r:
            r.raise_for_status()
            total = int(r.headers.get("content-length", 0))
            
            with open(filename, "wb") as f:
                for chunk in r.iter_bytes(chunk_size=8192):
                    f.write(chunk)
                    if total:
                        # print(f"Downloading: {r.num_bytes_downloaded/total*100:.1f}%")
                        logger.info(f"Downloading: {r.num_bytes_downloaded/total*100:.1f}%")

        
        # print("Download complete!")
        logger.info("Download complete!")
    
    except httpx.HTTPError as e:
        # print(f"Download failed: {str(e)}")
        logger.error(f"Download failed: {str(e)}")
        raise Exception(f"Download failed: {str(e)}")


# ** test **
# test_url = "https://arxiv.org/abs/2412.14174"
# download_paper(test_url, "test.pdf")