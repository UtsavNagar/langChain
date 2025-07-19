from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me a name, age and the city of a finctional person \n {formate_instruction}",
    input_variables=[],
    partial_variables={'formate_instruction': parser.get_format_instructions()}
)

chain = template | model | parser
response = chain.invoke({})
print("Response:", response)
