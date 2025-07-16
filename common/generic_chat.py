from common.chat_history import load_history_markdown, append_to_history_markdown, initialize_history_file

def run_openai_chat_loop(
    client, model_name, history_file, 
    temperature=0.8, max_tokens=4096, top_p=1
):
    """
    Generic loop for OpenAI-compatible chat clients.
    """
    load_context_choice = input("Do you want to load previous conversation history for context? (yes/no): ").strip().lower()
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    if load_context_choice == "yes":
        for entry in load_history_markdown(history_file):
            messages.append({"role": "user", "content": entry['prompt']})
            messages.append({"role": "assistant", "content": entry['response']})
        print(f"\n✅ Loaded previous context from {history_file}.")
    else:
        initialize_history_file(history_file)
        print(f"\n🚀 Starting fresh. {history_file} cleared.")

    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ").strip()
        if prompt.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        messages.append({"role": "user", "content": prompt})
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p
        )
        answer = response.choices[0].message.content
        print("\nAI Response:\n")
        print(answer)

        messages.append({"role": "assistant", "content": answer})
        append_to_history_markdown(history_file, prompt, answer)

        print(f"✅ Saved to {history_file}.")