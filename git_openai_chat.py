import os
from dotenv import load_dotenv
from openai import OpenAI
from common.generic_chat import run_openai_chat_loop

load_dotenv()
client = OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.getenv("GITHUB_KEY")
)

HISTORY_FILE = "git_openai_chat_history.md"

run_openai_chat_loop(
    client=client,
    model_name="openai/gpt-4.1",
    history_file=HISTORY_FILE,
    temperature=1,
    max_tokens=32768
)