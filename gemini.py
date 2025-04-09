#!/usr/bin/env python3
import os
from google import genai
from google.genai import types
# from google.api_core import exceptions as google_api_exceptions

def chat_loop_with_client():
    # --- 1. Get API Key ---
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        # ... (rest of the error message)
        return

    try:
        # --- 2. Initialize Client ---
        client = genai.Client(api_key=api_key)
        print("Client initialized successfully.")

        # --- 3. Choose Model ---
        model_name = "gemini-2.0-flash" # Or "gemini-1.0-pro", "gemini-pro" or your experimental one
        print(f"Using model: {model_name}")
        print("Starting chat. Type 'quit' or 'exit' to end the conversation.")

        # --- 4. Initialize Conversation History ---
        history = []

        # --- 5. Start the Chat Loop ---
        while True:
            # --- 5a. Get User Input ---
            user_input = input("\nYou: ")
            if not user_input:
                print("Please enter a message.")
                continue
            if user_input.lower() in ["quit", "exit"]:
                print("Exiting chat. Goodbye!")
                break

            # --- 5b. Add User Input to History ---
            history.append(types.Content(role="user", parts=[types.Part.from_text(text=user_input)]))

            # --- 5c. Configure Generation ---
            generation_config = types.GenerateContentConfig(
                response_mime_type="text/plain",
                # temperature=0.7
            )

            # --- 5d. Send History to Model via Client.models and Get Response ---
            print("Gemini: ", end="")
            full_response_text = ""
            try:
                # **** FIX HERE: Use client.models.generate_content_stream ****
                # **** Also use 'config=' keyword, not 'generation_config=' ****
                stream = client.models.generate_content_stream( # Correct method path
                    model=model_name,                          # Pass model name string
                    contents=history,
                    config=generation_config,                  # Use 'config' keyword
                    # No stream=True needed, method name implies it
                )

                # --- 5e. Print Streamed Response ---
                for chunk in stream:
                    if hasattr(chunk, 'text') and chunk.text:
                        print(chunk.text, end="")
                        full_response_text += chunk.text
                    # Alternative check... (kept for robustness)
                    # elif hasattr(chunk, 'parts') and chunk.parts:
                    #    for part in chunk.parts:
                    #        if hasattr(part, 'text') and part.text:
                    #             print(part.text, end="")
                    #             full_response_text += part.text
                print()

                # --- 5f. Add Model Response to History ---
                history.append(types.Content(role="model", parts=[types.Part.from_text(text=full_response_text)]))

                # Optional history pruning...

            except Exception as e:
                 print(f"\nAn error occurred during generation: {e}") # The error you saw happened here
                 if history and history[-1].role == "user":
                     print("Removing the last message from history due to error.")
                     history.pop()
                 print("Please try again.")
                 continue

    except Exception as e:
        # Catch errors during initial client setup
        print(f"\nAn error occurred during setup: {e}")

if __name__ == "__main__":
    chat_loop_with_client()
