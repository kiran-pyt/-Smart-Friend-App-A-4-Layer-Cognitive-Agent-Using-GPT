# decision.py
from pydantic import BaseModel
from openai import OpenAI

class DecisionInput(BaseModel):
    user_summary: str
    last_topic: str

class DecisionOutput(BaseModel):
    plan: str

class Decision:
    def __init__(self, client: OpenAI):
        self.client = client

    def decide(self, data: DecisionInput) -> DecisionOutput:
        system_msg = "You are a helpful friend who suggests fun ideas."

        reply = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": f"The user likes {data.last_topic}. Suggest one fun idea or fact about it."}
            ]
        )

        text = reply.choices[0].message.content.strip()
        return DecisionOutput(plan=text)
