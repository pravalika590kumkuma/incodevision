# Simple AI Chatbot

print(" Simple AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    # Exit condition
    if user == "bye":
        print("Chatbot: Goodbye! Have a nice day ")
        break

    # Predefined responses
    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Chatbot: I'm fine, thank you!")

    elif "your name" in user:
        print("Chatbot: I am a simple AI chatbot.")

    elif "help" in user:
        print("Chatbot: I can answer simple questions.")

    elif "weather" in user:
        print("Chatbot: I cannot check live weather yet, but it's a great day to learn Python!")

    elif "bye" in user:
        print("Chatbot: Goodbye!")
        break

    # Default response
    else:
        print("Chatbot: Sorry, I don't understand that.")