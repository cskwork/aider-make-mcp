from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List, Optional
from enum import Enum

app = FastAPI(
    title="MCP Server",
    description="Model Context Protocol Server",
    version="0.1.0"
)

class ContextType(str, Enum):
    DOCUMENT = "document"
    CODE = "code"
    DATA = "data"

class ContextRequest(BaseModel):
    query: str
    context_type: ContextType
    context: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, str]] = None
    options: Optional[Dict[str, str]] = None

class ContextResponse(BaseModel):
    response: str
    context_type: ContextType
    metadata: Dict[str, str]
    citations: List[Dict[str, str]] = []
    error: Optional[str] = None

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}

@app.post("/context")
async def handle_context(request: ContextRequest):
    """
    Handle MCP context requests according to official specification
    """
    try:
        # Example implementation for document context
        if request.context_type == ContextType.DOCUMENT:
            return {
                "response": f"Processed document query: {request.query}",
                "context_type": request.context_type.value,
                "metadata": {
                    "source": "mcp_server",
                    "context_used": request.context or {},
                    **(request.metadata or {})
                },
                "citations": [
                    {
                        "id": "doc1",
                        "title": "Sample Document",
                        "url": "http://example.com/doc1"
                    }
                ]
            }
        # Add other context type handlers here
        else:
            return {
                "response": f"Processed {request.context_type} query: {request.query}",
                "context_type": request.context_type.value,
                "metadata": {
                    "source": "mcp_server",
                    "context_used": request.context or {},
                    **(request.metadata or {})
                },
                "citations": []
            }
    except Exception as e:
        return {
            "response": "",
            "context_type": request.context_type.value,
            "metadata": {},
            "citations": [],
            "error": str(e)
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
