from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Streamlit UI
st.header("Research Tool")

paper_input = st.selectbox(
    "Select research paper name",
    ["select..", 
     "Attention is All You Need", 
     "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-oriented"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (7-9 paragraphs)"]
)

# Prompt template
template = load_prompt("researchTemplate.json")

# Only run when a paper is selected
if paper_input != "select..":
    # formatted_prompt = template.format(
    #     paper_input=paper_input,
    #     style_input=style_input,
    #     length_input=length_input
    # )

    # st.markdown("### Generated Prompt")
    # st.text(formatted_prompt)

    if st.button("Submit"):
        with st.spinner("Generating response..."):
            chain = template | model
            result = chain.invoke({
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input
            })

            st.markdown("### Response")
            st.text(result.content)
else:
    st.warning("Please select a research paper to generate a prompt.")
