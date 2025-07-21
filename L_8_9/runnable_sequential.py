from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about: {topic}',
    input_variables=["topic"],
)

prompt2 = PromptTemplate(
    template='Explain the following joke: {joke}',
    input_variables=["joke"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

chain = RunnableSequence(
    prompt1 | model | parser | prompt2 | model | parser
)

joke = chain.invoke({
    "topic": "programming"
})

print(f"Generated Joke: {joke}")