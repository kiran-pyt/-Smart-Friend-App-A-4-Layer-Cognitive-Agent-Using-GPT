# memory.py
from pydantic import BaseModel

class MemoryData(BaseModel):
    name: str = ""
    location: str = ""
    last_topic: str = ""

class Memory:
    def __init__(self):
        self.data = MemoryData()

    def store(self, name, location, topic):
        self.data.name = name
        self.data.location = location
        self.data.last_topic = topic

    def get_memory(self) -> MemoryData:
        return self.data
