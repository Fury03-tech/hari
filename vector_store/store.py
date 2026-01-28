from vector_store.chroma_client import get_collection

def store_vectors(chunks, embeddings, metadata):
   
    collection = get_collection()

    document_id = metadata["document_id"]
    source = metadata["source"]
    access_roles = metadata["access_roles"]
    version = metadata["version"]

    for index, chunk in enumerate(chunks):
        vector_id = f"{document_id}_v{version}_{index}"

        collection.add(
            ids=[vector_id],
            embeddings=[embeddings[index]],
            documents=[chunk],
            metadatas=[{
                "document_id": document_id,
                "source": source,
                "access_roles": access_roles,
                "version": version,
                "archived": False
            }]
        )
        

