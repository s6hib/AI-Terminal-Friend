# Necessary library imports
from rich.console import Console
from rich.theme import Theme
import openai
import os
import sys

# Set OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Set up console with new theme for different colors
custom_theme = Theme({
  "response": "bold cyan",
})
console = Console(theme=custom_theme)


# Function to request response from OpenAI
def request_response_from_openai(prompt: str) -> str:
  conversation_prompt = f"""
    You are my AI companion. Answer my questions with precision.

    Prompt: {prompt}
    """

  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{
      "role": "system",
      "content": conversation_prompt
    }],
    temperature=0.7,
  )

  # Extract and return the chat response from the OpenAI response
  return response.choices[0].message.content.strip()


# Main function
def run_assistant():
  # Gather all arguments as a single query string
  query = ' '.join(sys.argv[1:])

  # Fetch chat response from OpenAI
  chat_response = request_response_from_openai(query)

  # Display response to user
  console.print(f"[response]{chat_response}[/response]")


# Run the assistant when script is called
if __name__ == '__main__':
  run_assistant()
