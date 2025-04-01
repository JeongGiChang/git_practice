from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.chatgpt_service import ChatGPTService

router3 = APIRouter(prefix="/chat", tags=["ChatGPT"])

class ChatRequest(BaseModel):
    message: str

@router3.post("/message")
async def get_chatgpt_response(request: ChatRequest):
    try:
        service = ChatGPTService()
        response = service.generate_response(request.message)

        
        lines = response.split("\n")
        desc_lines = []
        table_lines = []
        in_table = False

        for line in lines:
            if line.strip().startswith("|"):
                in_table = True
            if in_table:
                table_lines.append(line)
            else:
                desc_lines.append(line)

        return {
            "description": "\n".join(desc_lines).strip(),
            "markdownTable": "\n".join(table_lines).strip()
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
