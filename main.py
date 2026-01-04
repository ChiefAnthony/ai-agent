import argparse
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompts import system_prompt


def main():
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise Exception("Missing GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    parser = argparse.ArgumentParser(description="AI-agent")
    parser.add_argument("user_prompt", type=str, help="Prompt to send to the AI agent")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # --- THE AGENT LOOP ---
    max_iterations = 20
    for i in range(max_iterations):
        if args.verbose:
            print(f"Iteration {i + 1}/{max_iterations}")

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=messages,
            config=types.GenerateContentConfig(
                tools=[available_functions], system_instruction=system_prompt
            ),
        )

        if not response.usage_metadata:
            raise RuntimeError("API request failed: No usage metadata returned")

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls:
            function_results = []

            for function_call in response.function_calls:
                function_call_result = call_function(
                    function_call, verbose=args.verbose
                )

                function_results.append(function_call_result.parts[0])

                if args.verbose:
                    print(
                        f"-> {function_call_result.parts[0].function_response.response}"
                    )

            messages.append(types.Content(role="user", parts=function_results))

        else:
            print(f"Final Response: {response.text}")
            return  # exit the program

    print("Error: Maximum iterations reached without a final response.")
    exit(1)


if __name__ == "__main__":
    main()
