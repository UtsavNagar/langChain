from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about topic: {topic}',
    input_variables=["topic"], 
)

prompt2 = PromptTemplate(
    template='generate a linked in post about: {topic}',
    input_variables=["topic"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': prompt1 | model | parser,
    'linkedin_post': prompt2 | model | parser
})

parallel_result = parallel_chain.invoke({
    "topic": "programming"
})

print(f"Generated Tweet: {parallel_result['tweet']}")
print(f"Generated LinkedIn Post: {parallel_result['linkedin_post']}")