# API Quick Start Guide

## Account Registration

### Registration Benefits

* 🎁 New users receive a free trial credit of **$0.2** upon registration.
* 💰 Minimum top-up amount: **$5**
* 🔗 Registration link: [Click to register](https://api.chainhub.tech/register)

## Configuration Steps

### 1. Obtain a Token

1. Log in to the backend system
2. Enter the "Token" page
3. Click "Add Token" to get the API Key.

### 2. Interface Configuration

#### BASE\_URL (Optional address)

```
https://api.chainhub.tech
https://api.chainhub.tech/v1
https://api.chainhub.tech/v1/chat/completions
```

> **Note:** Different clients may require different BASE\_URLs. It is recommended to try the addresses listed above one by one.

### 3. Model selection

* The model name is located in the first column of the "Supported Models" list on the homepage.

## Test and verification

You can verify the configuration in the following ways:

1. Test online in the chat page
2. Test the API using an API tool (such as Postman).

### Configuration Example

```json
{
  "base_url": "https://api.chainhub.tech",
  "api_key": "your_token_here",
  "model": "selected_model_name"
}
```

> **Note:** It is recommended to test the configuration on the chat page first to confirm that it is correct before proceeding with development and integration.
