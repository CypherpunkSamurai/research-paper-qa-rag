# vector_store.py
# https://docs.llamaindex.ai/en/stable/examples/vector_stores/AWSDocDBDemo/
import os
from typing import List
from llama_index.core.schema import Document
from llama_index.core import StorageContext
from llama_index.core import VectorStoreIndex
from llama_index.core.vector_stores.types import BasePydanticVectorStore

# * Faiss Vector Store (Local)
# from llama_index.vector_stores.faiss import FaissVectorStore

# * Qdrant Vector Store
# import qdrant_client
# from llama_index.vector_stores.qdrant import QdrantVectorStore

# # * Pinecone Vector Store
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores.pinecone import PineconeVectorStore

# # * Milvus Vector Store
# from llama_index.vector_stores.milvus import MilvusVectorStore


VECTOR_STORE_API_KEY = os.getenv("VECTOR_STORE_API_KEY", None)


# def create_faiss_vector_store(store_name: str) -> BasePydanticVectorStore:
#     """
#     Create a vector store client.
#     """
#     return FaissVectorStore(faiss_index=store_name)


def create_pinecone_vector_store(store_name: str) -> BasePydanticVectorStore:
    """
    Create a vector store client.
    """
    # pc = Pinecone(api_key=VECTOR_STORE_API_KEY)
    # pinecone_index = pc.Index(store_name)
    # delete if necessary
    # pc.delete_index(store_name)
    # create if necessary
    # pc.create_index(
    #     name=store_name,
    #     # for FastEmbedEmbedding
    #     dimension=384,
    #     metric="euclidean",
    #     spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    # )

    # return
    return PineconeVectorStore(api_key=VECTOR_STORE_API_KEY, index_name=store_name)


# def create_milvus_vector_store(milvus_store_uri: str, store_name: str) -> BasePydanticVectorStore:
#     """
#     Create a vector store client.
#     """
#     # * NOTE: The URI can be a "milvus.db" file or a Milvus server URI like http://localhost:19530
#     # https://milvus.io/docs/quickstart.md
#     client = MilvusVectorStore(uri=milvus_store_uri, overwrite=True)
#     client.create_collection(
#         collection_name=store_name,
#         dimension=768,  # The vectors we will use in this demo has 768 dimensions
#     )


# def create_qdrant_vector_store(
#     store_host: str, store_port: int, store_name: str
# ) -> BasePydanticVectorStore:
#     """
#     Create a vector store client.
#     """
#     use_tls = True
#     # check if host is "localhost" or "127.0.0.1"
#     if store_host in ["localhost", "127.0.0.1"]:
#         use_tls = False

#     # create a Qdrant client
#     client = qdrant_client.QdrantClient(
#         # you can use :memory: mode for fast and light-weight experiments,
#         # it does not require to have Qdrant deployed anywhere
#         # but requires qdrant-client >= 1.1.1
#         # location=":memory:"
#         # otherwise set Qdrant instance address with:
#         # url="http://127.0.0.1:6333",
#         # otherwise set Qdrant instance with host and port:
#         host=store_host,
#         port=store_port,
#         https=use_tls,
#         # set API KEY for Qdrant Cloud
#         api_key="TEST",
#     )
#     # create a vector store (using files)
#     return QdrantVectorStore(client=client, collection_name=store_name)


def create_query_engine(
    vector_store: BasePydanticVectorStore, documents: List[Document]
) -> VectorStoreIndex:
    """
    Create a query engine from the vector store.
    """
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(
        documents,
        storage_context=storage_context,
    )
    # create a storage context
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    # set Logging to DEBUG for more detailed outputs
    return index.as_query_engine()
