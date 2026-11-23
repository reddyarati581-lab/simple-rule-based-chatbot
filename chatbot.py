import re

def chatbot():
    print("Welcome to Simple Chatbot!")
    print("Type 'bye' to exit.")

    while True:
        user = input("You: ").lower().strip()
        user = re.sub(r'[^a-z0-9 ]', '', user)

        if "hello" in user or "hi" in user:
            print("Bot: Hello! How can I help you?")

        elif "name" in user:
            print("Bot: I am a Simple Rule-Based Chatbot.")

        elif "how are you" in user:
            print("Bot: I am fine. Thank you!")

        elif "help" in user:
            print("Bot: Sure! How can I help you?")

        elif user == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
