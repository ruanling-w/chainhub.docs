# Simple Python function calling demo

# OpenAI Function Calling Sample Code

## Basic Settings

### Install dependencies

```bash
pip install openai
```

### Initialize the client

```python
from openai import OpenAI
import json

client = OpenAI(
    base_url="https://api.chainhub.tech/v1",
    api_key="sk-xxxxx"
)
```

## Implementation of Weather Query Function

### Simulated Weather Function

```python
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather at a specified location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps({"location": "San Francisco", "temperature": "72", "unit": unit})
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})
```

### Main Dialogue Function

```python
def run_conversation():
    # 1. Setting up the dialog and available functions
    messages = [{"role": "user", "content": "What's the weather like in San Francisco, Tokyo, and Paris?"}]
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        },
                        "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                    },
                    "required": ["location"],
                },
            },
        }
    ]

    # 2. Create a conversation
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )

    response_message = response.choices[0].message
    print(response_message)

    # 3. Handling function calls
    tool_calls = response_message.tool_calls
    if tool_calls:
        available_functions = {
            "get_current_weather": get_current_weather,
        }

        messages.append(response_message)

        # 4. Execute the function call and obtain the result.
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)

            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )

            messages.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": function_name,
                "content": function_response,
            })

        # 5. Obtain the final response
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )
        return second_response

# Execute Dialogue
print(run_conversation())
```

### Key Features

* Supports multi-turn dialogues
* Automated function calls
* Result formatting
* Error handling mechanism

### Notes

* Requires correct API key configuration
* Ensure stable network connection
* Be aware of API call limitations
* Handle potential JSON parsing errors
