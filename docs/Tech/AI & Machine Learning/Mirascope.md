## Connect it to ollama

```python
# set your OPENAI_API_KEY in your .env 
from openai.types.chat import ChatCompletionMessageParam
from mirascope.openai import OpenAICall

class Librarian(OpenAICall):
    prompt_template = """
    SYSTEM: You are the world's greatest librarian.
    MESSAGES: {history}
    USER: {question}
    """
    question: str
    history: list[ChatCompletionMessageParam] = []

librarian = Librarian(question="", history=[])
while True:
    librarian.question = input("(User): ")
    response = librarian.call()
    librarian.history += [
        {"role": "user", "content": librarian.question},
        {"role": "assistant", "content": response.content},
    ]
    print(f"(Assistant): {response.content}")


# connecting ollama/llama3 
from openai.types.chat import ChatCompletionMessageParam
from mirascope.openai import OpenAICall, OpenAICallParams

class Librarian(OpenAICall):
    prompt_template = """
    SYSTEM: You are the world's greatest librarian.
    MESSAGES: {history}
    USER: {question}
    """
    question: str
    history: list[ChatCompletionMessageParam] = []
    api_key = "ollama"
    base_url = "http://localhost:11434/v1/"
    call_params = OpenAICallParams(model="llama3")


librarian = Librarian(question="", history=[])
while True:
    librarian.question = input("(User): ")
    response = librarian.call()
    librarian.history += [
        {"role": "user", "content": librarian.question},
        {"role": "assistant", "content": response.content},
    ]
    print(f"(Assistant): {response.content}")
```
