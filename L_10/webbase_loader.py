from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

prompt = PromptTemplate(
    input_variables=["text", "question"],
    template="Answer the following question {question} about the following text: {text}",
)

parser = StrOutputParser()

loader = WebBaseLoader("https://www.amazon.in/Apple-MacBook-13-inch-10-core-Unified/dp/B0DZDDQ429")
docs = loader.load()

chain = prompt | model | parser

question = input("Enter your question: ")
if not question:
    question = "What is the product specification?"

print(chain.invoke({'text': docs[0].page_content, 'question': question}))