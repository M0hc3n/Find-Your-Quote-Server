def find_similar_quotes(query, vector_db, model, k=5):
    query_vector = model.encode([query])

    distances, indices = vector_db.search(query_vector.astype('float32'), k)
    return indices[0]