from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid

from ..models.embeddings import embed_text

# connect to local Qdrant
client = QdrantClient("localhost", port=6333)

COLLECTION = "research_memory"


def init_collection():
    client.recreate_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(
            size=384,
            distance=Distance.COSINE,
        )
    )


def embed(text: str):
    return embed_text(text)


def store_memory(user_id, text, meta):
    vector = embed(text)

    client.upsert(
        collection_name=COLLECTION,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={
                    "user": user_id,
                    "text": text,
                    **meta,
                },
            )
        ],
    )


def search_memory(query, user_id):
    vector = embed(query)

    results = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=5,
    )

    return results.points