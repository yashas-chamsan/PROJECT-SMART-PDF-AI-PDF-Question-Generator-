# 📄 AI PDF Question Generator

An AI-powered PDF Question Generator built using Retrieval-Augmented Generation (RAG). The application allows users to upload PDF documents, ask questions about their content, and automatically generate MCQs, short-answer, and long-answer questions.

---

## 🚀 Features

- 📄 Upload PDF documents
- 📖 Extract text from PDFs
- ✂️ Split text into semantic chunks
- 🧠 Create embeddings using Sentence Transformers
- 🔍 Store and search embeddings using FAISS
- 💬 Ask questions about uploaded PDFs
- ✅ Generate Multiple Choice Questions (MCQs)
- 📝 Generate Short Answer Questions
- 📚 Generate Long Answer Questions
- 🌐 Interactive Streamlit web interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- Sentence Transformers
- FAISS
- PyPDF2
- NumPy

---

## 📂 Project Structure

```
AI-PDF-QUESTION-GENERATOR/
│
├── src/
│   ├── pdf_loader.py
│   ├── text_splitter.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── llm.py
│   └── question_generator.py
│
├── data/
├── app.py
├── requirements.txt
├── README.md
└── .env
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yashas-chamsan/PROJECT-SMART-PDF-AI-PDF-Question-Generator-.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your Gemini API key:

```
GOOGLE_API_KEY=your_api_key
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. Upload a PDF.
2. Extract text from the document.
3. Split the text into smaller chunks.
4. Generate embeddings.
5. Store embeddings in a FAISS vector database.
6. Retrieve relevant chunks based on the user's question.
7. Use Google Gemini to generate answers and questions.

---

## 📸 Screenshots

- PDF Upload
- AI Question Answering
- MCQ Generation
- Short Answer Generation
- Long Answer Generation

---

## 🔮 Future Improvements

- Chat history
- Support multiple PDFs
- Download generated questions as PDF or DOCX
- Better UI/UX
- Cloud deployment

---

## 👨‍💻 Author

**Yashas Chamsan**

Artificial Intelligence Project – LaunchED Global