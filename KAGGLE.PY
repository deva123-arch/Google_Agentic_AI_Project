"""
================================================
 STUDY ASSISTANT AI AGENT (Gemini API Version)
================================================
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai

# --------------------------
# LOAD API KEY FROM .env
# --------------------------
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❗ ERROR: Gemini API key not found in .env")
    print("Please add:  GEMINI_API_KEY=xxxxx  to your .env file")
    exit()

# --------------------------
# CONFIGURE GEMINI CLIENT
# --------------------------
genai.configure(api_key=GEMINI_API_KEY)
MODEL = "gemini-2.5-flash"

# --------------------------
# MODEL CALL FUNCTION
# --------------------------
def call_model(prompt):
    try:
        response = genai.GenerativeModel(MODEL).generate_content(prompt)
        return response.text
    except Exception as e:
        return f"[ERROR contacting Gemini API: {e}]"


# --------------------------
# HIGH-LEVEL FEATURES
# --------------------------
def summarize_text(text):
    prompt = f"Summarize this text into concise bullet points:\n\n{text}"
    return call_model(prompt)

def explain_topic(topic):
    prompt = f"Explain '{topic}' in simple language like you would to a beginner."
    return call_model(prompt)

def generate_quiz(topic, n=5):
    prompt = f"Generate a {n}-question MCQ quiz with answers for: {topic}"
    return call_model(prompt)

def create_flashcards(topic, n=10):
    prompt = f"Create {n} flashcards for topic '{topic}' in format: Q -> A"
    return call_model(prompt)

def study_plan(subject, days=5):
    prompt = f"Give a {days}-day structured study plan for learning {subject}"
    return call_model(prompt)

def motivational_boost():
    prompt = "Give a short motivational message for studying."
    return call_model(prompt)


# --------------------------
# MAIN INTERFACE
# --------------------------
def run_agent():
    print("\n======================================")
    print("   STUDY ASSISTANT AI (Gemini Only)   ")
    print("======================================")
    print("Type 'menu' to see options, 'exit' to quit.\n")

    while True:
        cmd = input("You: ").strip()

        if cmd in {"exit", "quit"}:
            print("Goodbye & good luck studying! 👋")
            break

        if cmd == "menu":
            print("""
OPTIONS:
1  - Summarize text
2  - Explain topic
3  - Generate quiz
4  - Create flashcards
5  - Study plan
6  - Motivation
7  - Chat with AI
menu - show options
exit - quit
""")
            continue

        # MENU OPTIONS
        if cmd == "1":
            txt = input("Paste text:\n")
            print("\n--- SUMMARY ---")
            print(summarize_text(txt))
            print("-------------------\n")
            continue

        if cmd == "2":
            t = input("Topic: ")
            print("\n--- EXPLANATION ---")
            print(explain_topic(t))
            print("-------------------\n")
            continue

        if cmd == "3":
            t = input("Topic: ")
            n = input("No. of questions [default 5]: ")
            n = int(n) if n else 5
            print("\n--- QUIZ ---")
            print(generate_quiz(t, n))
            print("-------------------\n")
            continue

        if cmd == "4":
            t = input("Topic: ")
            n = input("Number of flashcards [default 10]: ")
            n = int(n) if n else 10
            print("\n--- FLASHCARDS ---")
            print(create_flashcards(t, n))
            print("-------------------\n")
            continue

        if cmd == "5":
            s = input("Subject: ")
            d = input("Days [default 5]: ")
            d = int(d) if d else 5
            print("\n--- STUDY PLAN ---")
            print(study_plan(s, d))
            print("-------------------\n")
            continue

        if cmd == "6":
            print("\n--- MOTIVATION ---")
            print(motivational_boost())
            print("-------------------\n")
            continue

        if cmd == "7":
            q = input("\nAsk AI:\n")
            print("\nAI:", call_model(q), "\n")
            continue

        # Default → treat as chat
        print("\nAI:", call_model(cmd), "\n")


if __name__ == "__main__":
    run_agent()
