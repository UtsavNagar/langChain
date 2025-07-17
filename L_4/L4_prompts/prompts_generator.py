from langchain_core.prompts import PromptTemplate

# Prompt template
template = PromptTemplate(
    template="""
    Please explain the research paper titled '{paper_input}' in a {style_input} manner.
    The explanation should be {length_input}, focusing on clarity and relevance.
    """,
    input_variables=['paper_input', 'style_input', 'length_input'],
    validate_template=True
)

template.save("researchTemplate.json")