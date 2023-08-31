import requests
import json

# CricAPI settings
api_key = 'cric_api_key'
base_url = 'base_url'
params = {
    'apikey': api_key,
    'offset': 0
}

# Telegram Bot settings
bot_token = 'bot token given from botfather'
chat_id = 'group or personal chatid'

# Get cricket match data from CricAPI
response = requests.get(base_url, params=params)
data = response.json()

try:
    for item in data["data"]:
        if "score" in item:
            score = item["score"]
            # Convert the score dictionary to a formatted JSON string
            score_json = json.dumps(score, indent=4)

            # Telegram API endpoint URL
            send_message_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            # Parameters for the Telegram message
            message_params = {
                'chat_id': chat_id,
                'text': score_json
            }

            # Send the message to the Telegram group
            telegram_response = requests.post(send_message_url, params=message_params)

            if telegram_response.ok:
                print('Score message sent successfully.')
            else:
                print('Score message sending failed.')

except Exception as e:
    print("Error:", e)

