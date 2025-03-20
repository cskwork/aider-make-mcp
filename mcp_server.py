from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Dict, List, Optional, Union
from enum import Enum
import json

app = FastAPI(
    title="MCP Server",
    description="Model Context Protocol Server",
    version="0.1.0",
    openapi_url="/openapi.json"
)

class ContextType(str, Enum):
    DOCUMENT = "document"
    CODE = "code"
    DATA = "data"

class ContextRequest(BaseModel):
    query: str
    context_type: ContextType
    context: Optional[Dict[str, Union[str, List[str]]]] = None
    metadata: Optional[Dict[str, str]] = None
    options: Optional[Dict[str, Union[str, bool, int]]] = None

class Citation(BaseModel):
    id: str
    title: str
    url: Optional[str] = None
    text: Optional[str] = None

class ContextResponse(BaseModel):
    response: str
    context_type: ContextType
    metadata: Dict[str, str]
    citations: List[Citation] = []
    error: Optional[str] = None

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "version": "0.1.0",
        "capabilities": {
            "context_types": [ct.value for ct in ContextType],
            "max_query_length": 1000,
            "supports_streaming": False
        }
    }

@app.post("/context")
async def handle_context(request: Request):
    """
    Handle MCP context requests according to official specification
    """
    try:
        body = await request.json()
        context_request = ContextRequest(**body)
        
        # Process based on context type
        if context_request.context_type == ContextType.DOCUMENT:
            return {
                "response": f"Processed document query: {context_request.query}",
                "context_type": context_request.context_type.value,
                "metadata": {
                    "source": "mcp_server",
                    "context_used": context_request.context or {},
                    **(context_request.metadata or {})
                },
                "citations": [
                    {
                        "id": "doc1",
                        "title": "Sample Document",
                        "text": "This is a sample document text",
                        "url": "http://example.com/doc1"
                    }
                ]
            }
        else:
            return {
                "response": f"Processed {context_request.context_type} query: {context_request.query}",
                "context_type": context_request.context_type.value,
                "metadata": {
                    "source": "mcp_server",
                    "context_used": context_request.context or {},
                    **(context_request.metadata or {})
                },
                "citations": []
            }
    except Exception as e:
        return {
            "response": "",
            "context_type": body.get("context_type", "document"),
            "metadata": {},
            "citations": [],
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
