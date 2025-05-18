# faq_search.py

import pickle
import numpy as np
from numpy.linalg import norm
from .embedding_utils import embed_query

# Load precomputed FAQ index
with open("services/faq_index.pkl", "rb") as f:
    faq_index = pickle.load(f)

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (norm(vec1) * norm(vec2))

def find_best_faq_answer(user_question, threshold=0.7):
    user_vec = embed_query(user_question)
    if not user_vec:
        return {"match_question": None, "answer": None, "similarity": 0}

    best_score = -1
    best_entry = None

    for item in faq_index:
        score = cosine_similarity(user_vec, item["embedding"])
        if score > best_score:
            best_score = score
            best_entry = item

    if best_score < threshold:
        return {"match_question": None, "answer": None, "similarity": round(best_score, 4)}

    return {
        "match_question": best_entry["question"],
        "answer": best_entry["answer"],
        "similarity": round(best_score, 4)
    }
