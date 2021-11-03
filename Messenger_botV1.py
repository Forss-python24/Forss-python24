import config
import requests



class Messenger_bot():

    def __init__(self) -> None:
        pass
    
    def SendAPI(self, senderID, response_msg):

        PAGE_ACCESS_TOKEN = config.PAGE_ACCESS_TOKEN

        print(f"sendAPI senderID is {senderID}")
        payload = {
            'messaging_type': 'RESPONSE',
            'recipient': {'id':senderID},
            'message': response_msg
        }

        headers = {"content-type": "application/json"}

        url = f"https://graph.facebook.com/v2.6/me/messages?access_token={PAGE_ACCESS_TOKEN}"
        resp = requests.post(url, json=payload, headers=headers)

    def handleMessage(self, senderID, message_obj):

        if 'text' in message_obj:

            self.SendAPI(senderID, "Hello from this class!")