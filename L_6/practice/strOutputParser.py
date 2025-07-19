from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

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

prompt1 = template1.invoke({"topic": "The impact of AI on modern society"})
response1 = model.invoke(prompt1.text)

prompt2 = template2.invoke({"report": response1.content})
response2 = model.invoke(prompt2)

print("Detailed Report:" + response1.content)