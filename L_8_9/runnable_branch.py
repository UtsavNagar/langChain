from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence,RunnableBranch, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_cnt(word):
    return len(word.split())

prompt1 = PromptTemplate(
    template='Generate a detailed report on topic: {topic}',
    input_variables=["topic"], 
)

prompt2 = PromptTemplate(
    template='Summaries the following text: {text}',
    input_variables=["text"], 
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

report_generation_chain = RunnableSequence(
    prompt1 | model | parser
)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300,prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = report_generation_chain | branch_chain

response = final_chain.invoke({'topic': 'Artificial Intelligence'})

print(response)