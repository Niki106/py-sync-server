from fastapi import FastAPI, Response
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    nip: str
    email: str
    category: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/webhooks", status_code=200)
async def handle_webhook(item: Item):
    print(item)  # Example: Print the payload for debugging
    
    return {"message": "Webhook received successfully"}