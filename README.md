# Model Context Protocol (MCP) Server

A basic implementation of Anthropic's Model Context Protocol for connecting AI systems to data sources.

## Features
- REST API implementation of MCP
- Context-aware request handling
- Extensible architecture for future integrations
- FastAPI-based server

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

## API Endpoints
- POST /context
  - Request: { "query": "your query", "context": {} }
  - Response: { "response": "Hello World! You asked: your query", "metadata": {} }

## Future Plans
- Add authentication and security
- Implement data source integrations
- Add support for streaming responses
- Implement context caching
