import json
import os

import requests

tunnels = requests.get("http://127.0.0.1:4040/api/tunnels").content
tunnels = json.loads(tunnels)["tunnels"]
https_tunnels = list(
    filter(
        lambda tunnel: tunnel["proto"] == "https"
        and "ngrok.io" in tunnel["public_url"],
        tunnels,
    )
)

current_tunnel = https_tunnels[0]["public_url"]
print(f"Current_tunnel: {current_tunnel}")

bot_token = os.environ.get("BOT_TOKEN")
request = (
    f"https://api.telegram.org/bot{bot_token}/setWebhook?"
    f"url={current_tunnel}/{bot_token}&"
    'allowed_updates=["message"]'
)
print(f"Request: {request}")

response = requests.get(request)
print(f"Response: {response}")
