from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate detailed report on: {topic}',
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template='Generate 5 pointer summary on the following: {text}',
    input_variables=["text"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

response = chain.invoke({
    "topic": "The impact of climate change on global agriculture"
})

print(response)
chain.get_graph().print_ascii()