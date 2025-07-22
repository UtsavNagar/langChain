from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="practice/data/sample.csv", encoding="utf-8")  # ✅ correct relative path
documents = loader.lazy_load()
for doc in documents:
    print(doc.page_content)  # ✅ print the content of each document
    print(doc.metadata)  # ✅ print the metadata of each document