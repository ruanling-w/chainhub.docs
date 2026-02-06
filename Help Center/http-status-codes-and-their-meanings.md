# HTTP Status Codes and Their Meanings

HTTP status codes are 3-digit codes used to indicate the status of an HTTP response from a web server. Below are some common HTTP status codes and their meanings:

| Status Code                  | Explanation                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| 400 Bad Request              | The request format is incorrect or cannot be understood by the server. Usually indicates a client error.                       |
| 401 Unauthorized             | API key authentication failed. You need to verify whether your API key is correct; other reasons may include token expiration. |
| 403 Forbidden                | Generally means insufficient permissions.                                                                                      |
| 404 Not Found                | The requested resource was not found. You may be trying to access a non-existent endpoint.                                     |
| 413 Request Entity Too Large | The request body is too large. You may need to reduce the size of your request body.                                           |
| 429 Too Many Requests        | You have exceeded your rate limit due to too many frequent requests.                                                           |
| 500 Internal Server Error    | Internal server error. This may be an issue with the OpenAI server, not your problem.                                          |
| 503 Service Unavailable      | The server is temporarily unavailable. This may be due to OpenAI maintenance or server overload.                               |

> **Note**: The above are only some of the HTTP status codes and not a complete list. Some codes may vary depending on server implementation and usage.
