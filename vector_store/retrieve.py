from vector_store.chroma_client import get_collection
def retrieve_chunks(
    query_embedding,
    user_role,
    document_id=None,
    version=None,
    top_k=5
):
    collection = get_collection()

    where_clause = {
        "archived": False
    }

    # RBAC filter
    where_clause["access_roles"] = {"$in": [user_role]}

    # Optional document scoping
    if document_id:
        where_clause["document_id"] = document_id

    # Optional version scoping
    if version:
        where_clause["version"] = version

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=where_clause,
        include=["documents", "metadatas", "distances"]
    )

    return {
        "vector_ids": results["ids"][0],
        "chunks": results["documents"][0],
        "metadatas": results["metadatas"][0],
        "scores": results["distances"][0]
    }
