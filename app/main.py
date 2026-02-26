import os
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()
SLACK_TOKEN = os.getenv('SLACK_BOT_TOKEN')

class MessageRequest(BaseModel):
    channel: str
    text: str

@app.post("/notify")
def notify(req: MessageRequest):
    if not SLACK_TOKEN:
        return {"error": "Token not set"}
    url = "https://slack.com/api/chat.postMessage"
    headers = {"Authorization": f"Bearer {SLACK_TOKEN}"}
    resp = requests.post(url, headers=headers, json={"channel": req.channel, "text": req.text})
    return {"sent": resp.status_code == 200}