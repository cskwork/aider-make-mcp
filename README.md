# Model Context Protocol (MCP) Server

An implementation of Anthropic's Model Context Protocol following the official specification.

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

## Claude Desktop Integration

1. Start the MCP server
2. Open Claude Desktop app
3. Go to Settings > Integrations > MCP Servers
4. Add a new server with:
   - Name: Local MCP Server
   - URL: http://localhost:8000
5. Test the connection using the "Test Connection" button
6. Once connected, you can use the MCP server in your conversations by prefixing queries with `@mcp`

Example conversation:
```
@mcp What can you tell me about this code?
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
