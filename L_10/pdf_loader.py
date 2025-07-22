from langchain_community.document_loaders import PyPDFLoader
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

loader = PyPDFLoader("practice/data/UtsavProjectFileUpdated.pdf")
documents = loader.load()

print(f"Number of pages loaded: {len(documents)}")  # Debugging line to check number of pages

# chain = prompt | model | parser

# print(chain.invoke({'poem': documents[0].page_content}))
