from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from conversation import create_conversation, delete_conversation, get_all_conversations
from message import add_message, get_messages, delete_messages

app = FastAPI()

# CORS cho frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------- Request Models ---------
class MessageRequest(BaseModel):
    conversation_id: str
    input: str
    output: str

# --------- Endpoints ---------

@app.post("/conversations")
def new_conversation():
    conversation_id = create_conversation()
    return {"conversation_id": conversation_id}

@app.get("/conversations")
def get_conversations():
    conversations = get_all_conversations()
    return [
        {
            "conversation_id": str(conv["_id"]),
            "name": conv.get("name", ""),
            "createdAt": conv["createdAt"].isoformat(),
            "updatedAt": conv["updatedAt"].isoformat()
        }
        for conv in conversations
    ]

@app.delete("/conversations/{conversation_id}")
def delete_conv(conversation_id: str):
    delete_conversation(conversation_id)
    delete_messages(conversation_id)
    return {"status": "deleted"}

@app.post("/messages")
def add_new_message(req: MessageRequest):
    add_message(req.conversation_id, req.input, req.output)
    return {"status": "success", "input": req.input, "output": req.output}

@app.get("/messages")
def get_history(conversation_id: str):
    messages = get_messages(conversation_id)
    return [
        {
            "input": msg["input"],
            "output": msg["output"],
            "createdAt": msg["createdAt"].isoformat()
        }
        for msg in messages
    ]



# pip install fastapi uvicorn pymongo python-dotenv pydantic
# uvicorn server:app --reload --port 8000