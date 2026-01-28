from vector_store.chroma_client import get_collection


def is_document_archived(document_id, version=None):

    collection = get_collection()

    where_filter = {
        "document_id": document_id,
        "archived": True
    }

    if version is not None:
        where_filter["version"] = version

    results = collection.get(
        where=where_filter,
        limit=1
    )

    return len(results.get("ids", [])) > 0


def archive_document(document_id, version=None):
    collection = get_collection()

    if is_document_archived(document_id, version):
        return {
            "status": "noop",
            "message": "Document is already archived"
        }

    where_filter = {
        "document_id": document_id
    }

    if version is not None:
        where_filter["version"] = version

    collection.update(
        where=where_filter,
        metadatas=[{"archived": True}]
    )

    return {
        "status": "archived",
        "message": "Document archived successfully"
    }
