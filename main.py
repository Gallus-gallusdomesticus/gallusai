import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

def main():
    load_dotenv()

    args=[arg for arg in sys.argv[1:] if arg!="--verbose"]
    if not args:
        print("Gallus AI Code how to use")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "What is the scientific name of chicken?"')
        sys.exit(1)

    user_prompt=" ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    generate_content(client, messages)

def generate_content(client, messages):
    response=client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

    if "--verbose" in sys.argv:
        print("User prompt:")
        print(response.text)
        x=response.usage_metadata.prompt_token_count
        y=response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {x}")
        print(f"Response tokens: {y}")
    else:
        print(response.text)

    


if __name__ == "__main__":
    main()


