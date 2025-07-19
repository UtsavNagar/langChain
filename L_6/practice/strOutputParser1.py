from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template="Generate a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)


# # 2nd prompt -> summary
template2 = PromptTemplate(
    template="Summarize in 5 lines the following report: {report}",
    input_variables=["report"]
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

response = chain.invoke({
    "topic": "The impact of AI on modern society"
})

print(response)