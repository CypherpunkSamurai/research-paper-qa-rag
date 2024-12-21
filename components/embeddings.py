# embeddings.py
import os

# * FastEmbedEmbedding (Local)
from llama_index.embeddings.fastembed import FastEmbedEmbedding

# * Nomic AI
# https://docs.nomic.ai/atlas/models/text-embedding
# import nest_asyncio
# nest_asyncio.apply()
# from llama_index.embeddings.nomic import NomicEmbedding

# * Together.AI
# https://docs.together.ai/docs/serverless-models#embedding-models
# from llama_index.embeddings.together import TogetherEmbedding

# * VoyageAI
# https://docs.voyageai.com/docs/embeddings
# from llama_index.embeddings.voyageai import VoyageEmbedding

EMBEDDINGS_API_KEY = os.getenv("EMBEDDINGS_API_KEY", None)

# Embedding Models

embed_model = FastEmbedEmbedding(model_name="BAAI/bge-small-en-v1.5")

# embed_model = NomicEmbedding(
#     api_key=EMBEDDINGS_API_KEY,
#     model_name=[
#         "nomic-embed-text-v1",
#         "nomic-embed-text-v1.5",
#         "gte-multilingual-base",
#     ],
# )

# embed_model = TogetherEmbedding(
#     api_key=EMBEDDINGS_API_KEY,
#     model_name=[
#         "togethercomputer/m2-bert-80M-2k-retrieval",
#         "togethercomputer/m2-bert-80M-8k-retrieval",
#         "togethercomputer/m2-bert-80M-32k-retrieval",
#         "WhereIsAI/UAE-Large-V1",
#         "BAAI/bge-large-en-v1.5",
#         "BAAI/bge-base-en-v1.5",
#         "sentence-transformers/msmarco-bert-base-dot-v5",
#         "bert-base-uncased",
#     ][1],
# )

# embed_model = VoyageEmbedding(
#     model_name=[
#         "voyage-3-large",
#         "voyage-3",
#         "voyage-3-lite",
#         "voyage-code-3",
#         "voyage-finance-2",
#         "voyage-law-2",
#         "voyage-code-2",
#     ][1],
#     voyage_api_key=EMBEDDINGS_API_KEY,
# )
