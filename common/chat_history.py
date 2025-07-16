import os
from datetime import datetime

def load_history_markdown(history_file):
    """
    Parses a Markdown chat history file into a list of
    {"prompt": ..., "response": ...}
    """
    history_data = []
    if not os.path.exists(history_file):
        return history_data

    with open(history_file, "r") as f:
        lines = f.readlines()

    user_content = ""
    assistant_content = ""
    mode = None
    for line in lines:
        if line.startswith("### 👤 User:"):
            mode = "user"
            user_content = ""
        elif line.startswith("### 🤖 Assistant:"):
            mode = "assistant"
            assistant_content = ""
        elif line.startswith("---"):
            if user_content and assistant_content:
                history_data.append({
                    "prompt": user_content.strip(),
                    "response": assistant_content.strip()
                })
            user_content = ""
            assistant_content = ""
            mode = None
        else:
            if mode == "user":
                user_content += line
            elif mode == "assistant":
                assistant_content += line
    return history_data

def append_to_history_markdown(history_file, prompt, response):
    """
    Appends a conversation turn to the Markdown file.
    """
    with open(history_file, "a") as f:
        f.write(f"## 🗓 {datetime.now().isoformat()}\n")
        f.write(f"### 👤 User:\n{prompt}\n\n")
        f.write(f"### 🤖 Assistant:\n{response}\n\n---\n\n")

def initialize_history_file(history_file):
    """
    Creates the markdown file with a header if it does not exist or clears it.
    """
    with open(history_file, "w") as f:
        f.write("# Conversation History\n\n")