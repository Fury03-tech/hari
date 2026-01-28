from vector_store.chroma_client import get_collection

def delete_vectors_by_ids(vector_ids):

    if not vector_ids:
        return

    collection = get_collection()
    collection.delete(ids=vector_ids)


def delete_document_vectors(document_id, version=None):
    
    collection = get_collection()

    where_filter = {"document_id": document_id}

    if version is not None:
        where_filter["version"] = version

    collection.delete(where=where_filter)

