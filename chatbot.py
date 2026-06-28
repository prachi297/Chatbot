# ─────────────────────────────────────────────
#  Task 4: Basic Rule-Based Chatbot
#  Concepts: if-elif, functions, loops, I/O
# ─────────────────────────────────────────────

def get_reply(user_input):
    """Return a predefined reply based on the user's input."""
    msg = user_input.lower().strip()

    if "hello" in msg or "hi" in msg or "hey" in msg:
        return "Hi there!  How can I help you?"

    elif "how are you" in msg or "how do you do" in msg:
        return "I'm doing great, thanks for asking! "

    elif "bye" in msg or "goodbye" in msg or "exit" in msg:
        return "Goodbye! Have a wonderful day! "

    elif "your name" in msg or "who are you" in msg:
        return "I'm a simple rule-based chatbot!"
    
    elif "what is a chatbot?" in msg or "define chatbot" in msg:
        return "A chatbot is a software application or web interface designed to converse through text or speech."
    
    elif "what is coding?" in msg or "define coding" in msg:
        return "Coding tells a machine which actions to perform and how to complete tasks."

    elif "help" in msg or "what can you do" in msg:
        return "Try saying: hello, how are you, your name, or bye."

    else:
        return "I'm not sure how to respond. Try 'hello', 'how are you', or 'bye'."


def main():
    print("=" * 40)
    print("       Welcome to the Chatbot!")
    print("  (type 'bye' or 'exit' to quit)")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:          # skip empty input
            continue

        reply = get_reply(user_input)
        print(f"Bot: {reply}")

        # Exit the loop if the user said goodbye
        if any(word in user_input.lower() for word in ["bye", "goodbye", "exit"]):
            break


if __name__ == "__main__":
    main()