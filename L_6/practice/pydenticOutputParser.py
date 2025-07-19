from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

class Person(BaseModel):
    name: str = Field(description="Name of the fictional person")
    age: int = Field(gt=18,description="Age of the fictional person")
    city: str = Field(description="City where the fictional person lives")
    
parser = PydanticOutputParser(pydantic_object=Person)
template = PromptTemplate(
    template="Give me a name, age and the city of a {place} person \n {format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
response = chain.invoke({"place": "British"})
print("Response:", response)