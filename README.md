# Rule-Based Chatbot

A simple text-based chatbot built in Python using `if-elif` logic, functions, and loops — no external libraries required.

## Demo

```
========================================
       Welcome to the Chatbot!
  (type 'bye' or 'exit' to quit)
========================================

You: hello
Bot: Hi there! How can I help you?

You: how are you
Bot: I'm doing great, thanks for asking! 

You: what is your name
Bot: I'm a simple rule-based chatbot!

You: bye
Bot: Goodbye! Have a wonderful day! 
```

## Features

- Responds to greetings: `hello`, `hi`, `hey`
- Answers status queries: `how are you`
- Handles farewells: `bye`, `goodbye`, `exit`
- Answers identity questions: `who are you`, `your name`
- Offers help: `help`, `what can you do`
- Graceful fallback for unknown inputs

## Getting Started

**Requirements:** Python 3.x (no extra packages needed)

```bash
# Clone the repo
git clone https://github.com/your-username/chatbot.git
cd chatbot

# Run the chatbot
python chatbot.py
```

## Project Structure

```
chatbot/
│
├── chatbot.py   # Main chatbot script
└── README.md    # Project documentation
```

## How It Works

```
User Input
    │
    ▼
get_reply(user_input)
    │
    ├── "hello" / "hi"      → "Hi there! "
    ├── "how are you"       → "I'm doing great!"
    ├── "bye" / "exit"      → "Goodbye!" + exits loop
    ├── "your name"         → "I'm a simple chatbot!"
    ├── "help"              → Lists available commands
    └── anything else       → Fallback response
```

## Key Concepts Used

| Concept | Usage |
|---|---|
| `if-elif-else` | Keyword matching for replies |
| Functions | `get_reply()` and `main()` |
| `while` loop | Keeps conversation going |
| `input()` / `print()` | Console I/O |
| String methods | `.lower()`, `.strip()`, `in` |

## Extending the Bot

To add a new response, add an `elif` block inside `get_reply()`:

```python
elif "weather" in msg:
    return "I can't check the weather, but it's always sunny in Python! "
```

## License

MIT — free to use and modify.
