# action.py
from pydantic import BaseModel

class ActionInput(BaseModel):
    message: str

class ActionOutput(BaseModel):
    result: str

class Action:
    def execute(self, data: ActionInput) -> ActionOutput:
        return ActionOutput(result=f"🤖 Smart Friend says: {data.message}")
