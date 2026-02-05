# gpt realtime模型调用

```python
# example requires websocket-client library:
# pip install websocket-client

import os
import json
import websocket


url = "ws://api.chainhub.tech/v1/realtime?model=gpt-4o-realtime-preview"
headers = [
    "Authorization: Bearer sk-xxx" ,
    "OpenAI-Beta: realtime=v1"
]

def decode_unicode_string(s):
    """Decode Unicode strings to make Chinese characters readable."""
    try:
        # Try decoding directly first.
        if isinstance(s, bytes):
            return s.decode('utf-8')
        # If the string is already garbled, encode it first and then decode it.
        return s.encode('latin1').decode('utf-8')
    except Exception as e:
        print(f"Decoding failed: {e}")
        return s

def on_error(ws, error):
    print("\n=== Error message ===")
    print(f"{error}")
    
def on_close(ws, close_status_code, close_msg):
    print("\n=== Connection closed ===")
    print(f"Status code: {close_status_code}")
    print(f"Close message: {close_msg}")

def on_open(ws):
    print("\n=== Connection established ===")
    
    event = {
        "type": "response.create",
        "response": {
            "modalities": ["text"],
            "instructions": "Please assist the user."
        }
    }
    print("\n=== Send message ===")
    print(json.dumps(event, ensure_ascii=False, indent=2))
    ws.send(json.dumps(event))

def on_message(ws, message):
    print("\n=== Received message ===")
    try:
        data = json.loads(message)
        # If an error message is present, decode and display Chinese characters.
        if 'error' in data and 'message' in data['error']:
            data['error']['message'] = decode_unicode_string(data['error']['message'])
        
        print(json.dumps(data, ensure_ascii=False, indent=2))
        
        # If it is an error message, display a simplified version.
        if data.get('type') == 'error':
            print("\n=== Error summary ===")
            print(f"Error type: {data['error'].get('type', 'unknown')}")
            print(f"Error code: {data['error'].get('code', 'unknown')}")
            error_message = decode_unicode_string(data['error'].get('message', 'unknown'))
            print(f"Error message: {error_message}")
            
    except json.JSONDecodeError as e:
        print(f"Failed to parse message: {message}")
        print(f"Error: {e}")

# Enable websocket logging, but only display key information
websocket.enableTrace(False)

ws = websocket.WebSocketApp(
    url,
    header=headers,
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

print("\n=== Start connection ===")
print(f"Connection address: {url}")
ws.run_forever()


```
