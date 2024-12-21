import os
# load env before loading custom modules
from dotenv import load_dotenv
load_dotenv() 

# import llms
from components.llm import llm
from components.embeddings import embed_model

# vector store (import what you need, e.g. Faiss, Pinecone, Milvus, Qdrant are included)
from components.vector_store import create_query_engine, create_pinecone_vector_store

# import arxiv
from arxiv import download_paper, parse_paper_id

import log
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader


# Settings Configuration
Settings.llm = llm
Settings.embed_model = embed_model


def main():
    paper_url = "https://arxiv.org/abs/2412.14174"
    paper_id = parse_paper_id(paper_url)
    print(f"Downloading paper {paper_id}...")
    download_paper(paper_url, os.path.join(os.getcwd(), "documents", f"{paper_id}.pdf"))

    # embed to vector db
    print("Generating embeddings...")
    documents = SimpleDirectoryReader(
        os.path.join(os.getcwd(), "documents")
    ).load_data()

    # create a quadrant vector store
    vs = create_pinecone_vector_store("arxiv")
    # create a query engine
    query_engine = create_query_engine(vs, documents)

    # query the engine
    response = query_engine.query(
        "what are all the training methods to personalize image diffusion models in a list"
    )
    print(response)


if __name__ == "__main__":
    # test llm
    # response = llm.complete("write a python hello world program.")
    # print(response)

    # run main
    main()