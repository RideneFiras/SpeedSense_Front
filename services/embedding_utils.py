# embedding_utils.py

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def embed_query(text: str) -> list:
    """
    Returns the Gemini embedding of a given query.
    """
    try:
        response = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_query"
        )
        return response["embedding"]
    except Exception as e:
        print(" Error during embedding:", e)
        return []
