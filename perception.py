# perception.py
from pydantic import BaseModel
from openai import OpenAI

# What the user tells us
class UserPreference(BaseModel):
    name: str
    location: str
    favorite_topic: str

# What we understand about the user
class PerceptionOutput(BaseModel):
    interpreted_text: str

class Perception:
    def __init__(self, client: OpenAI):
        self.client = client

    def clean_text(self, text: str) -> str:
        # Remove unwanted phrase
        return text.replace("Download prompt test", "")

    def interpret(self, user_pref: UserPreference) -> PerceptionOutput:
        name = self.clean_text(user_pref.name)
        place = self.clean_text(user_pref.location)
        topic = self.clean_text(user_pref.favorite_topic)

        # Friendly system message for the LLM
        system_msg = f"You are a friendly helper. The user is {name} from {place} and likes {topic}."

        # Ask GPT to describe this user nicely
        reply = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_msg},
                {"role": "user", "content": "Describe this user in 2 simple lines."}
            ]
        )

        text = reply.choices[0].message.content.strip()
        return PerceptionOutput(interpreted_text=text)
