from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    "practice/data/books",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()  # Load all PDF files in the specified directory

for doc in docs:
    print(f"Loaded document with {len(doc.page_content)} characters.")
    # You can process each document as needed, e.g., summarization, etc.