from fastapi import FastAPI, Response
from pydantic import BaseModel

from app import order

app = FastAPI()

STORE_HASH = "5byitdbjtb"
API_TOKEN = "t4iu0pxpzxck0h5azrwmy8u3w9994q2"
BIGBUY_API_KEY = "YzhmYWFlMDFjMTA2YTZjZjRhYzhjMjg1NGViOGUwYTYzYjk1YTNjOGY4MDY3NzM1NzgyNzNhNzhiMDY5NGJiZA"  # sandbox

class Data2(BaseModel):
    type: str
    id: int

class Item(BaseModel):
    store_id: str
    producer: str
    scope: str
    data: Data2
    hash: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/webhooks", status_code=200)
async def handle_webhook(item: Item):
    # Get the order from BigCommerce and submit to BigBuy
    order_sender = order.OrderSender(STORE_HASH, API_TOKEN, BIGBUY_API_KEY)
    order_data = order_sender.get_and_send_order(item.data.id)
    print(order_data)
    
    return {"message": "Webhook received successfully"}

    