# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from agents.plan_agent import generate_plan
from agents.tool_agent import execute_task
from agents.feedback_loop import feedback_check
from agents.reflection import reflect_on_task
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
#######################
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to ["http://localhost"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#######################
load_dotenv()

class AgentRequest(BaseModel):
    query: str

@app.post("/run-agent")
def run_agent(request: AgentRequest):
    plan = generate_plan(request.query)
    results = []

    for task in plan:
        result = execute_task(task)
        if not feedback_check(result):
            modified_task = reflect_on_task(task)
            result = execute_task(modified_task)
        results.append({"task": task, "result": result})

    return {"query": request.query, "results": results}

