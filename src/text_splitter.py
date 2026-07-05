from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Splits the extracted PDF text into smaller chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_text(text)

    return chunks