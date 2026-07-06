import numpy as np


def retrieve_chunks(index, model, chunks, question, k=5):
    """
    Retrieves the most relevant chunks for a user's question.
    """

    question_embedding = model.encode([question])

    question_embedding = np.array(question_embedding).astype("float32")

    distances, indices = index.search(question_embedding, k)

    retrieved_chunks = []

    for idx in indices[0]:
        retrieved_chunks.append(chunks[idx])

    return retrieved_chunks