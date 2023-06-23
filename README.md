# AI Terminal Friend

AI Terminal Friend is a Python-based application that serves as an AI assistant in your terminal. It uses OpenAI's GPT-3.5-turbo model to answer any questions you might have. The app aims to make information retrieval more interactive and fun, treating your terminal as a conversation place with your AI companion.

### Prerequisites

- Python 3.7 or higher
- OpenAI Python client (openai>=0.27.0)

To install the required Python package, use pip:

```bash
pip install openai
```

You will also need to sign up on the OpenAI website to get your API key, which will allow you to use the GPT-3.5-turbo model.

### Installing

Firstly, clone the repository to your local machine:

```bash
git clone https://github.com/s6hib/AI-Terminal-Friend.git
cd AI-Terminal-Friend
```

Then, set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY='your-openai-api-key'
```

### Running the Application

To run the application, simply execute the Python script with your query:

```bash
python main.py 'your query here'
```

The AI will provide an answer to your query in the terminal.

## How it Works

AI Terminal Friend is primarily composed of a single Python file, `main.py`, which handles communication with the OpenAI API and formats the response in the terminal.

Here's a rundown of how the script works:

1. **Initialization:** The script initializes the OpenAI API with your key and sets up a stylized console for displaying responses.

2. **Response Request:** The `request_response_from_openai` function constructs a message prompt using your query and sends a request to the OpenAI API to get a response.

3. **Response Handling:** The function then extracts the response from the API's reply and returns it.

4. **Display:** The main function, `run_assistant`, fetches the chat response from the function and displays it on the console.
