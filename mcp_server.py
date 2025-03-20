from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional
from enum import Enum

app = FastAPI()

class ContextType(str, Enum):
    TEXT = "text"
    CODE = "code"
    DATA = "data"

class ContextRequest(BaseModel):
    query: str
    context_type: ContextType
    context: Optional[Dict[str, Any]] = None
    metadata: Optional[Dict[str, Any]] = None

class ContextResponse(BaseModel):
    response: str
    context_type: ContextType
    metadata: Dict[str, Any]
    error: Optional[str] = None

@app.post("/context", response_model=ContextResponse)
async def handle_context(request: ContextRequest):
    """
    Handle MCP context requests according to the official specification
    """
    try:
        # Basic implementation that returns a formatted response
        return ContextResponse(
            response=f"Processed {request.context_type} query: {request.query}",
            context_type=request.context_type,
            metadata={
                "source": "mcp_server",
                "context_used": request.context or {},
                **(request.metadata if request.metadata else {})
            }
        )
    except Exception as e:
        return ContextResponse(
            response="",
            context_type=request.context_type,
            metadata={},
            error=str(e)
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
