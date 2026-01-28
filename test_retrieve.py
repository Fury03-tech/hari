from vector_store.retrieve import retrieve_chunks

# Dummy query embedding
query_embedding = [0.1, 0.0, 0.0, 0.0]

results = retrieve_chunks(
    query_embedding=query_embedding,
    user_role="hr",
    top_k=2
)

print("Retrieved chunks:")
for chunk in results["chunks"]:
    print("-", chunk)
