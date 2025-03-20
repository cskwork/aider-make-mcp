from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

class ContextRequest(BaseModel):
    query: str
    context: Dict[str, Any] = {}

class ContextResponse(BaseModel):
    response: str
    metadata: Dict[str, Any] = {}

@app.post("/context", response_model=ContextResponse)
async def handle_context(request: ContextRequest):
    """
    Handle MCP context requests and return relevant information
    """
    try:
        # Basic implementation that just returns a hello world response
        return ContextResponse(
            response=f"Hello World! You asked: {request.query}",
            metadata={
                "source": "example_mcp_server",
                "context_used": request.context
            }
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
