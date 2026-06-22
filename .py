import random
from datetime import datetime

print("=" * 60)
print("🤖 SMART RULE-BASED CHATBOT")
print("=" * 60)

user_name = ""

jokes = [
    "😂 Why do programmers prefer dark mode? Because light attracts bugs!",
    "😂 Why did Python go to school? To improve its class!",
    "😂 Why do Java developers wear glasses? Because they don't C#."
]

motivations = [
    "🌟 Success comes from consistency, not perfection.",
    "🚀 Keep learning. Every expert was once a beginner.",
    "💡 Small progress every day adds up to big results.",
    "🏆 Believe in yourself and never stop growing."
]

while True:

    user_input = input("\nYou: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey", "hii", "good morning", "good evening"]:
        print("Bot: 👋 Hello! Nice to meet you.")

    # Name
    elif "my name is" in user_input:
        user_name = user_input.replace("my name is", "").strip().title()
        print(f"Bot: 😊 Nice to meet you, {user_name}!")

    elif "what is my name" in user_input:
        if user_name:
            print(f"Bot: Your name is {user_name}.")
        else:
            print("Bot: I don't know your name yet.")

    # About Bot
    elif user_input == "who are you":
        print("Bot: 🤖 I am a Smart Rule-Based Chatbot built using Python.")

    elif user_input == "what can you do":
        print("""
📌 I can:
✔️ Greet users
✔️ Remember your name
✔️ Tell date and time
✔️ Perform calculations
✔️ Tell jokes
✔️ Give motivation
✔️ Answer basic questions
✔️ Exit safely
        """)

    # Date
    elif "date" in user_input:
        today = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: 📅 Today's date is {today}")

    # Time
    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: ⏰ Current time is {current_time}")

    # Joke
    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))

    # Motivation
    elif "motivate" in user_input or "motivation" in user_input:
        print("Bot:", random.choice(motivations))

    # AI
    elif "artificial intelligence" in user_input or user_input == "ai":
        print("""
🤖 Artificial Intelligence (AI)

AI is the simulation of human intelligence in machines.
Applications:
✔️ Chatbots
✔️ Self-driving cars
✔️ Voice assistants
✔️ Recommendation systems
✔️ Healthcare
        """)

    # Python
    elif "python" in user_input:
        print("""
🐍 Python

Python is a popular programming language.
Features:
✔️ Easy to learn
✔️ Powerful libraries
✔️ Used in AI, ML, Web Development, Data Science
        """)

    # Machine Learning
    elif "machine learning" in user_input:
        print("""
📚 Machine Learning

Machine Learning enables computers to learn from data
without explicit programming.

Types:
✔️ Supervised Learning
✔️ Unsupervised Learning
✔️ Reinforcement Learning
        """)

    # Data Science
    elif "data science" in user_input:
        print("""
📊 Data Science

Data Science combines:
✔️ Statistics
✔️ Programming
✔️ Data Analysis
✔️ Machine Learning

Used for extracting insights from data.
        """)

    # Cyber Security
    elif "cyber security" in user_input:
        print("""
🔒 Cyber Security

Protecting systems and networks from attacks.

Key Areas:
✔️ Network Security
✔️ Ethical Hacking
✔️ Cloud Security
✔️ Information Security
        """)

    # Calculator
    elif user_input.startswith("calculate"):
        try:
            expression = user_input.replace("calculate", "").strip()
            result = eval(expression)
            print(f"Bot: 🧮 Result = {result}")
        except:
            print("Bot: Invalid calculation.")

    # Help
    elif user_input == "help":
        print("""
Available Commands:

👋 hi
😊 my name is <name>
❓ what is my name
🕒 time
📅 date
😂 joke
🚀 motivation
🐍 python
🤖 ai
📊 data science
📚 machine learning
🔒 cyber security
🧮 calculate 5+5
❌ exit
        """)

    # Exit
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: 👋 Thank you for chatting. Have a great day!")
        break

    # Default
    else:
        print("Bot: 🤔 Sorry, I don't understand that. Type 'help'.")

print("\nProgram Ended Successfully!")