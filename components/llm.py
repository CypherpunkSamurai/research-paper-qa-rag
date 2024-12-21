# llm.py
import os

# * Groq
from llama_index.llms.groq import Groq
# * Ollama
# from llama_index.llms.ollama import Ollama
# * Gemini
# from llama_index.llms.gemini import Gemini
# * OpenRouter
# from llama_index.llms.openrouter import OpenRouter

LLM_API_KEY = os.getenv("LLM_API_KEY", None)

# *create a large language model client

llm = Groq(
    model=[
        "llama-3.3-70b-versatile",
        "llama-3.3-70b-specdec",
        "llama-3.2-3b-preview",
        "llama-3.2-1b-preview",
        "llama-3.1-8b-instant",
        "gemma2-9b-it",
        "mixtral-8x7b-32768",
        "llama3-groq-70b-8192-tool-use-preview",
        "llama3-groq-8b-8192-tool-use-preview",
    ][0],
    api_key=LLM_API_KEY,
)

# llm = Ollama(
#     model=[
#         "qwq",
#         "mistral",
#         "mistral-nemo",
#         "mistral-small",
#         "tinyllama",
#         "falcon3",
#     ][0]
# )

# llm = Gemini(
#     model=[
#         "gemini-2.0-flash-exp",
#         "gemini-1.5-flash",
#         "gemini-1.5-flash-8b",
#         "gemini-1.5-pro",
#     ][3],
#     api_key=LLM_API_KEY,
# )

# llm = OpenAI(model="gpt-4", api_key=LLM_API_KEY)

# llm = OpenRouter(
#     model=[
#         "mistralai/mistral-7b-instruct:free",
#         "qwen/qwen-2-7b-instruct:free",
#         "meta-llama/llama-3.1-70b-instruct:free",
#         "google/gemini-2.0-flash-exp:free",
#         "google/gemini-exp-1206:free",
#     ][0],
#     api_key=LLM_API_KEY,
# )
