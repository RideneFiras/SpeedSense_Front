# generate_faq_index.py

import os
import pickle
from embedding_utils import embed_query
from faq_data import faq_list

faq_index = []

print("🔄 Embedding FAQ questions...")
for i, item in enumerate(faq_list):
    embedding = embed_query(item["question"])
    if embedding:
        faq_index.append({
            "question": item["question"],
            "answer": item["answer"],
            "embedding": embedding
        })
        print(f"✅ Q{i+1} embedded")
    else:
        print(f"❌ Q{i+1} failed")

# Save to file
with open("faq_index.pkl", "wb") as f:
    pickle.dump(faq_index, f)

print("✅ All done! Saved to faq_index.pkl")
