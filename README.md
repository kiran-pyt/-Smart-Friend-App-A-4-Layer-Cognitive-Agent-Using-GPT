# -Smart-Friend-App-A-4-Layer-Cognitive-Agent-Using-GPT

🤖 Smart Friend App — 4 Layer Cognitive Agent with LLM

Welcome to Smart Friend App, a beginner-friendly Cognitive AI Agent built with Python + OpenAI GPT.
It demonstrates how an intelligent system can perceive, remember, decide, and act — just like a simple digital brain!

🧩 Overview

The agent runs in four logical layers:

Layer	File	Role
👁️ Perception	perception.py	Understands the user (uses LLM)
💾 Memory	memory.py	Stores user name, location & interests
🧠 Decision-Making	decision.py	Thinks & creates a helpful idea (uses LLM)
⚡ Action	action.py	Shows the final message
🧩 Prompt Evaluator	prompt_evaluator.py	Checks prompt quality
🎬 Main Controller	main.py	Connects all layers
🧠 How It Works (Step by Step)

1️⃣ User tells their name, location, and favorite topic.
2️⃣ Perception Layer uses GPT to describe the user in simple words.
3️⃣ Memory Layer saves that information.
4️⃣ Decision Layer asks GPT for a fun or useful suggestion.
5️⃣ Action Layer displays it neatly.
6️⃣ Prompt Evaluator prints a JSON review of a sample prompt.

Example run:

🌟 Welcome to Smart Friend App 🌟
What is your name? Kiran
Where are you from? Sullurpeta
What do you like learning about? AI

👀 Perception Layer says:
Kiran from Sullurpeta loves learning about AI and its creative uses.

💾 Memory saved your info!

🧠 Decision Layer says:
Why not try creating AI art using DALL-E or Midjourney?

⚡ Action Layer says:
🤖 Smart Friend says: Why not try creating AI art using DALL-E or Midjourney?

🧩 Prompt Evaluator Result:
{
 "explicit_reasoning": true,
 "structured_output": true,
 "tool_separation": true,
 "conversation_loop": true,
 "instructional_framing": true,
 "internal_self_checks": false,
 "reasoning_type_awareness": false,
 "fallbacks": false,
 "overall_clarity": "Excellent structure, but could improve with self-checks and error fallbacks."
}

🛠️ Setup & Run
# 1 Clone this repo
git clone https://github.com/<your-username>/SmartFriendApp.git
cd SmartFriendApp

# 2 Install dependencies
pip install openai pydantic python-dotenv

# 3 Add your API key
echo OPENAI_API_KEY=sk-yourkey > .env

# 4 Run the app
python main.py

🧱 Project Structure
SmartFriendApp/
├── perception.py         # 👁️ Understands user (LLM)
├── memory.py             # 💾 Stores preferences
├── decision.py           # 🧠 Generates suggestion (LLM)
├── action.py             # ⚡ Displays result
├── prompt_evaluator.py   # 🧩 Prompt checker
├── main.py               # 🎬 Connects everything
└── README.md

✅ Assignment Checklist
Requirement	Status
Four modules (Perception, Memory, Decision, Action)	✅
main.py connects all layers	✅
Asks user preferences before flow	✅
Feeds preferences into prompt	✅
Cleans phrase “Download prompt test”	✅
Uses LLM in Perception & Decision	✅
Uses Pydantic for data models	✅
Has Prompt Evaluator JSON output	✅
Well-documented README for GitHub	✅
Ready for YouTube demo	✅
🎥 YouTube Demo (Upload link here)

Record your screen showing the program run and add your link below:

🎬 YouTube Demo: https://youtu.be/GSwGRJ5MeMQ

💡 Learning Outcomes
Concept	You Learn
Cognitive Architecture	How AI systems think in layers
LLM Integration	Use GPT for understanding & decision
Prompt Engineering	Write and clean prompts for reasoning
Pydantic	Validate structured inputs/outputs
Python Modules	Organize code cleanly
AI Explainability	See each layer’s output clearly
