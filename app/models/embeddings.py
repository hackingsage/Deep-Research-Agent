from sentence_transformers import SentenceTransformer

# lightweight CPU embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2",
    device="cpu"
)

def embed_text(text: str):
    vector = model.encode(text)
    return vector.tolist()