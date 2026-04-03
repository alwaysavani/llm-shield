from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .core.masker import LLMMasker
import uvicorn

app = FastAPI(
    title="LLM-Shield",
    description="API for masking PII before sending data to LLMs.",
    version="0.1.0"
)

masker = LLMMasker()

class MaskRequest(BaseModel):
    text: str

class MaskResponse(BaseModel):
    masked_text: str
    entities_found: list[str]

@app.get("/")
def read_root():
    return {"message": "Welcome to LLM-Shield. Use /mask to sanitize your prompts."}

@app.post("/mask", response_model=MaskResponse)
async def mask_text(request: MaskRequest):
    """
    Endpoint to mask PII in the provided text.
    """
    if not request.text:
        raise HTTPException(status_code=400, detail="Text cannot be empty.")

    try:
        result = masker.mask(request.text)
        return MaskResponse(
            masked_text=result["masked_text"],
            entities_found=list(set(result["entities"]))
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
