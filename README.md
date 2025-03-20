# Model Context Protocol (MCP) Server

An implementation of Anthropic's Model Context Protocol following the official specification from [https://modelcontextprotocol.io](https://modelcontextprotocol.io)

This server implements the MCP v1.0 specification and provides:

## Core Features
- Document context processing with citation support
- Code context processing with language-specific handling
- Data context processing with structured results
- Health check endpoint with capabilities reporting
- Error handling and validation
- Support for context-specific options

## Features
- REST API implementation of MCP
- Support for text, code, and data context types
- Proper error handling and metadata support
- FastAPI-based server
- Aligned with official MCP specification

## Requirements
- Python 3.8+
- FastAPI
- Uvicorn

## Installation
```bash
pip install fastapi uvicorn
```

## Running the Server
```bash
python mcp_server.py
```

## Client Configuration

To configure an MCP server in your client application, add the following to your configuration:

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```

### Key Configuration Options:
- `command`: The command to run the server (e.g., "uv" for uvicorn)
- `args`: Arguments to pass to the command
  - `--directory`: Path to the server's parent directory
  - `run`: Command to start the server
  - Server filename (e.g., "weather.py")

## Claude Desktop Integration Guide

### Prerequisites
1. Claude Desktop app installed (version 1.2.0 or later)
2. Python 3.8+ installed
3. MCP server running locally
4. Proper client configuration as shown above

### Step-by-Step Setup

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the MCP Server**
   ```bash
   python mcp_server.py
   ```
   The server will start on http://localhost:8000

3. **Configure Claude Desktop**
   - Open Claude Desktop app
   - Go to Settings > Integrations > MCP Servers
   - Click "Add New Server"
   - Enter the following details:
     - Name: Local MCP Server
     - URL: http://localhost:8000
     - Description: Local MCP server for testing
   - Click "Save"

4. **Test the Connection**
   - In the MCP Servers list, click the "Test Connection" button next to your server
   - You should see a green checkmark if the connection is successful

5. **Using MCP in Conversations**
   - Start a new conversation in Claude Desktop
   - Use the `@mcp` prefix to route queries to your MCP server
   - Example queries:
     ```
     @mcp Analyze this code snippet: [your code here]
     @mcp What can you tell me about this document?
     @mcp Process this data: [your data here]
     ```

### Troubleshooting
- **Connection Failed**: Ensure the MCP server is running and accessible
- **Timeout Errors**: Check your network settings and firewall rules
- **Invalid Responses**: Verify the server logs for any errors

### Example Conversation Flow
```
User: @mcp What can you tell me about this code?
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

Claude: [MCP Response] Processed code query: This appears to be a recursive implementation of the factorial function...
```

## API Endpoints
- POST /context
  - Request: 
    ```json
    {
      "query": "your query",
      "context_type": "text|code|data",
      "context": {},
      "metadata": {}
    }
    ```
  - Response:
    ```json
    {
      "response": "Processed response",
      "context_type": "text|code|data",
      "metadata": {},
      "error": null
    }
    ```

## Future Plans
- Add authentication and security
- Implement data source integrations
- Add support for streaming responses
- Implement context caching
- Add support for context versioning
