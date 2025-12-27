import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file")

client = OpenAI(api_key=API_KEY)

def ask_ai(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def main():
    print("AI CLI Assistant")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Goodbye.")
            break

        if not user_input:
            print("Please enter a prompt.")
            continue

        try:
            answer = ask_ai(user_input)
            print(f"\nAI: {answer}\n")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
