from vector_store.store import store_vectors

# Dummy data (pretend backend already chunked & embedded)
chunks = [
    "HR policy about leave",
    "Employee onboarding process"
]

embeddings = [
    [0.1, 0.0, 0.0, 0.0],
    [0.1, 0.0, 0.0, 0.0]
]

metadata = {
    "document_id": 1,
    "source": "hr_policy.pdf",
    "access_roles": "hr",
    "version": 1
}

store_vectors(chunks, embeddings, metadata)

print(" Test store completed")
