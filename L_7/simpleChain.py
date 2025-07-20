from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template='Generate 5 interesting points about the following question: {input}',
    input_variables=["input"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({
    "input": "What are the benefits of using AI in healthcare?"
})

print(result)

chain.get_graph().print_ascii()