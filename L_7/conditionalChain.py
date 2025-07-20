from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash"
)

parser = StrOutputParser()


class FeedbackClassification(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(..., description="The sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=FeedbackClassification)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following text into positive or negative: \n {feedback} \n {format_instructions}',
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classification_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Generate a response to the following positive feedback: \n {feedback}',
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template='Generate a response to the following negative feedback: \n {feedback}',
    input_variables=["feedback"]
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),               # if sentiment is positive
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),               # else if sentiment is negative
    RunnableLambda(lambda x: f"No response needed for sentiment: {x.sentiment}")    # else case (optional, can be omitted if not needed)
)

chain = classification_chain | branch_chain

print(chain.invoke({
    "feedback": "This product is terrible than I expected!, device is not working as expected. and the customer service was unhelpful."
}))

chain.get_graph().print_ascii()