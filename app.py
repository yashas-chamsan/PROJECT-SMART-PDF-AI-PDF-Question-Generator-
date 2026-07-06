import streamlit as st
import os

from src.pdf_loader import extract_text_from_pdf
from src.text_splitter import split_text
from src.embeddings import create_embeddings, model
from src.vector_store import create_vector_store
from src.retriever import retrieve_chunks
from src.llm import generate_answer
from src.question_generator import generate_questions

st.set_page_config(
    page_title="AI PDF Question Generator",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Question Generator")

st.markdown("""
Welcome!

This application can:

- 📄 Read PDF files
- 🤖 Answer questions from PDFs
- 📝 Generate MCQs
- 📚 Generate Short Answer Questions
- 📖 Generate Long Answer Questions
""")

uploaded_file = st.file_uploader(
    "Upload a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    os.makedirs("data/uploads", exist_ok=True)

    save_path = os.path.join("data/uploads", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"Uploaded: {uploaded_file.name}")

    st.write("✅ PDF saved successfully!")

    with st.spinner("Processing PDF..."):

        text = extract_text_from_pdf(save_path)

        chunks = split_text(text)

        embeddings = create_embeddings(chunks)

        index = create_vector_store(embeddings)

    st.success("✅ AI is ready!")

    st.divider()

    st.subheader("Ask a question about your PDF")

    question = st.text_input("")

    if st.button("Get Answer"):

        with st.spinner("Thinking..."):

            context_chunks = retrieve_chunks(
                index=index,
                model=model,
                chunks=chunks,
                question=question,
                k=5
            )

            context = "\n\n".join(context_chunks)

            answer = generate_answer(question, context)

        st.subheader("Answer")

        st.write(answer)

    st.divider()

    st.subheader("Generate Questions")

    if st.button("Generate Questions"):

        with st.spinner("Generating questions..."):

            questions = generate_questions(text)

        st.subheader("Generated Questions")

        st.write(questions)