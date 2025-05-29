from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(temperature=0)

prompt = PromptTemplate.from_template(
    """Given a user request: '{input}',
    break it down into a list of tasks. List them step by step."""
)

plan_chain = prompt | llm

def generate_plan(user_input: str) -> list:
    result = plan_chain.invoke({"input": user_input})
    return [step.strip() for step in result.content.split("\n") if step.strip()]

# ################################################
# it's dummy code, replace with real LLM
####################################################

# from langchain_core.language_models.fake import FakeListLLM
###################################
# Use fake model to mock LLM response
######################################
# llm = FakeListLLM(responses=[
#     "Sure, here is a simple one-week Europe trip plan:\nDay 1: Paris\nDay 2: Amsterdam\nDay 3: Berlin\nDay 4: Prague\nDay 5: Vienna\nDay 6: Venice\nDay 7: Rome"
# ])
