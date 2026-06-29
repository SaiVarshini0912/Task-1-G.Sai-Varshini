print("🤖 Welcome to Rule-Based AI Chatbot")
print("Type 'help' to see available commands")
print("Type 'exit' to quit")

from datetime import datetime
while True:
    user = input("\nYou: ").lower().strip()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    elif user == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user in ["what is your name", "your name"]:
        print("Bot: My name is Rule-Based AI Chatbot.")

    elif user == "course":
        print("Bot: You are studying engineering/computer science.")

    elif user in ["date","todays date","what is the date today"]:
        print("Bot: Today's date is", datetime.now().date())

    elif user == "time":
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))
    
    elif user in ["python","what is python"]:
        print("Bot: Python is a popular programming language used in AI, Web Development, and Data Science.")

    elif user in ["ai","what is ai"]:
        print("Bot: AI stands for Artificial Intelligence.")

    elif user in ["dsa","what is dsa"]:
        print("Bot: DSA stands for Data Structures and Algorithms.")

    elif user in ["internship","what is internship"]:
        print("Bot: Internships help you gain practical experience and improve your skills.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "help":
        print("You can say")
        print("- hello / hi / hey")
        print("- how are you")
        print("- your name")
        print("- college")
        print("- course")
        print("- python")
        print("- ai")
        print("- dsa")
        print("- internship")
        print("- thank you")
        print("- exit")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day. ")
        break

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available commands.")