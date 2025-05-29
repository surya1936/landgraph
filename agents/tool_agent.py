from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def dummy_tool(task: str) -> str:
    """A simple tool that simulates task execution."""
    return f"Executed task: {task}"

tools = [dummy_tool]

llm_tool = ChatOpenAI(temperature=0)
agent = initialize_agent(tools, llm_tool, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

def execute_task(task: str) -> str:
    return agent.run(task)
