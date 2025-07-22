from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

prompt = PromptTemplate(
    input_variables=["poem"],
    template="Write the summary for the following poem: {poem}",
)

parser = StrOutputParser()

loader = TextLoader("practice/data/sample.txt", encoding="utf-8")  # ✅ correct relative path
documents = loader.load()

chain = prompt | model | parser

print(chain.invoke({'poem': documents[0].page_content}))  # ✅ use the first document's content
