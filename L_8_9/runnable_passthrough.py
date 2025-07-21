from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a joke about topic: {joke}',
    input_variables=["joke"], 
)

prompt2 = PromptTemplate(
    template='generate explaination about joke: {joke}',
    input_variables=["joke"],
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

passthrough = RunnablePassthrough()

joke_generation_chain = RunnableSequence(
    prompt1 | model | parser
)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': prompt2 | model | parser
})

final_chain = RunnableSequence(joke_generation_chain | parallel_chain)   

result = final_chain.invoke({
    "joke": "programming"
})

print(f"Generated Joke: {result['joke']}")
print(f"Generated Explanation: {result['explanation']}")    