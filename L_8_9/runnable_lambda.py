from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

def word_cnt(word):
    return len(word.split())

prompt = PromptTemplate(
    template='Generate a joke about topic: {topic}',
    input_variables=["topic"], 
)

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()

joke_generation_chain = RunnableSequence(
    prompt | model | parser
)

runnable_parrallel = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_cnt' : RunnableLambda(word_cnt)
})

final_chain = RunnableSequence(joke_generation_chain, runnable_parrallel)

result = final_chain.invoke({'topic': 'AI'})

final_result = """{} \n word count - {}""".format(result['joke'],result['word_cnt'])

print(final_result)