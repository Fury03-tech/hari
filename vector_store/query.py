from vector_store.chroma_client import get_collection

def query_vectors(
    query_embedding,
    top_k=5
):
    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return {
        "vector_ids": results["ids"][0],
        "chunks": results["documents"][0],
        "metadatas": results["metadatas"][0],
        "scores": results["distances"][0]
    }

