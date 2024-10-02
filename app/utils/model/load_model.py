import faiss
import os

from sentence_transformers import SentenceTransformer

from utils.core.config import save_dir

def load_model():
    vector_db = faiss.read_index(os.path.join(save_dir, "faiss_index.bin"))
    
    model = SentenceTransformer(os.path.join(save_dir, "sentence_transformer"))
    
    print(f"Model loaded from {save_dir}")
    return vector_db, model