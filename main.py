from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# @app.post("/webhooks")
# async def handle_webhook(request: Request):
#     webhook_data = await request.json()  # Parse the JSON payload
#     # Process the data in webhook_data
#     print(webhook_data)  # Example: Print the payload for debugging
    
#     return {"message": "Webhook received successfully"}