import os
import sys

from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import available_functions, call_function

def main():
    load_dotenv()

    verbose="--verbose" in sys.argv

    args=[arg for arg in sys.argv[1:] if arg!="--verbose"]
    if not args:
        print("Gallus AI Code how to use")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "What is the scientific name of chicken?"')
        sys.exit(1)

    user_prompt=" ".join(args)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    generate_content(client, messages, verbose)



def generate_content(client, messages, verbose):

    response=client.models.generate_content(model="gemini-2.0-flash-001", contents=messages, 
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt))
    
    if verbose:
        x=response.usage_metadata.prompt_token_count
        y=response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {x}")
        print(f"Response tokens: {y}")

    if not response.function_calls:
        return response.text


    for function_call_part in response.function_calls:
        function_call_result=call_function(function_call_part)

        if not function_call_result.parts :
            raise Exception("Function parts not found")
        
        
        if not function_call_result.parts[0].function_response:
            raise Exception("Function response not found")

        if not function_call_result.parts[0].function_response.response:
            raise Exception("Response not found")
        
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")


    


if __name__ == "__main__":
    main()


