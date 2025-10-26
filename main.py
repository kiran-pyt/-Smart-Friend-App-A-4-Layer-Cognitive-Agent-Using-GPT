# main.py
import os
from dotenv import load_dotenv
from openai import OpenAI

from perception import Perception, UserPreference
from memory import Memory
from decision import Decision, DecisionInput
from action import Action, ActionInput
from prompt_evaluator import evaluate_prompt

load_dotenv()

def main():
    print("🌟 Welcome to Smart Friend App 🌟")
    print("Let's know you better!\n")

    # Ask user preferences (before flow)
    name = input("What is your name? ")
    place = input("Where are you from? ")
    topic = input("What do you like learning about? ")

    # Create OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # --- 1. Perception ---
    perception = Perception(client)
    user = UserPreference(name=name, location=place, favorite_topic=topic)
    p_out = perception.interpret(user)
    print("\n👀 Perception Layer says:")
    print(p_out.interpreted_text)

    # --- 2. Memory ---
    memory = Memory()
    memory.store(name, place, topic)
    mem = memory.get_memory()
    print("\n💾 Memory saved your info!")

    # --- 3. Decision ---
    decision = Decision(client)
    d_in = DecisionInput(user_summary=p_out.interpreted_text, last_topic=mem.last_topic)
    d_out = decision.decide(d_in)
    print("\n🧠 Decision Layer says:")
    print(d_out.plan)

    # --- 4. Action ---
    action = Action()
    result = action.execute(ActionInput(message=d_out.plan))
    print("\n⚡ Action Layer says:")
    print(result.result)

    # # --- 5. Prompt Test Evaluation ---
    # print("\n🧩 Running Prompt Test Evaluation...")
    # prompt_text = "You are a Prompt Evaluation Assistant. Evaluate prompts with clear step-by-step reasoning."
    # evaluation = evaluate_prompt(prompt_text)
    # print(evaluation.json(indent=2))

    # --- 5. Prompt Test Evaluation ---
    print("\n🧩 Running Prompt Test Evaluation...")
    prompt_text = "You are a Prompt Evaluation Assistant. Evaluate prompts with clear step-by-step reasoning."
    evaluation = evaluate_prompt(prompt_text)
    print(evaluation.model_dump_json(indent=2))  # ✅ FIXED LINE

    print("\n🎯 All done! You built your first Cognitive Agent!")


  

if __name__ == "__main__":
    main()
