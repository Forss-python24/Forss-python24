from flask import Flask, request
import json
import requests
import config


app = Flask(__name__)

app.config['SECRET_KEY'] = 'FOI2F-R24F9-NC234-DP94R'

def resp(text):

    return {'text':text}

def button(**kwargs):

    button = kwargs

    return button

def postback_buttons(text, *args):

    btn = []
    for arg in args:

        btn.append(arg)

    base = dict(attachment=dict(type='template',
     payload=dict(template_type='button', text=text, buttons=btn)))

    return base

def callSendAPI(senderID, response_msg):
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
    #print(resp.text)

def postbackHandler(senderID, postback):

    if postback == "bt1":

        response = {
            "attachment":{
                "type":"template",
                "payload":{
                    "template_type":"generic",
                    "elements":[
                    {
                        "title":"Welcome!",
                        "image_url":"https://omu.edu.ly/wp-content/uploads/2021/02/cropped-new-omu.png",
                        "subtitle":"This is the official OMU website!",
                        "default_action": {
                        "type": "web_url",
                        "url": "omu.edu.ly",
                        "webview_height_ratio": "compact",
                        },
                        "buttons":[
                        {
                            "type":"web_url",
                            "url":"omu.edu.ly",
                            "title":"View Website"
                        },{
                            "type":"postback",
                            "title":"Start Chatting",
                            "payload":"Chatting"
                        },{
                            "type":"postback",
                            "title":"Go back ⬅️",
                            "payload":"back1"
                        }               
                        ]      
                    }
                    ]
                }
            }
        }

        callSendAPI(senderID, response)
    elif postback == "bt2":

        response = {'text': "You pressed Button2 ! Congratulations"}
        callSendAPI(senderID, response)
    elif postback == "back1":

        bt1 = button(type='postback', title="Details", payload='bt1')
        bt2 = button(type='postback', title="What we offer", payload='bt2')

        callSendAPI(senderID, postback_buttons("Welcome, Press a button!", bt1, bt2))

    else:
        
        response = {"text": "Seems like i still cant understand that callback rightnow, maybe it's under development!.."}
        callSendAPI(senderID, response)

def handleMessage(senderID, message):

    if 'text' in message:

        if message['text'].lower() == "start":
            
            bt1 = button(type='postback', title="Details", payload='bt1')
            bt2 = button(type='postback', title="What we offer", payload='bt2')

            callSendAPI(senderID, postback_buttons("Welcome, Press a button!", bt1, bt2))
        
        elif message['text'].lower() == "hi":

            callSendAPI(senderID, resp("Hello, how are you?"))
        else:

            callSendAPI(senderID, resp(f"You sent ({message['text']})!"))
    else:
        response = {"text": "I only understand text! :("}
        callSendAPI(senderID, response)


@app.route('/', methods=['GET', 'POST'])
def home():
    return "<h1>HOME</h1>"


@app.route('/webhook', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':

        VERIFY_TOKEN = '2onif3d-9439ffdw-md2093fn2-0394vncwpm9423fv'

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print(mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print(f"this is the normal token {token}")
            print(token)
        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print(challenge)
        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')
            print(f"this is the and statment token {token}")

            if mode == 'subscribe' and token == VERIFY_TOKEN:

                print("WEBHOOK VERIFIED")

                challenge = request.args.get('hub.challenge')

                return challenge, 200

            else:
                return 'ERROR', 403

        data = request.data
        dataOBJ = json.loads(data.decode('utf-8'))

        print(f"Data object is {dataOBJ}")
        if 'object' in dataOBJ and dataOBJ['object'] == 'page':

            entries = dataOBJ['entry']
            for entry in entries:
                print(entry)
                webhookEvent = entry['messaging'][0]

                senderPsid = webhookEvent['sender']['id']

                if 'message' in webhookEvent:
                    handleMessage(senderPsid, webhookEvent['message'])

                    return 'EVENT_RECEIVED', 200
                else:
                    return 'ERROR', 404

    if request.method == 'POST':

            VERIFY_TOKEN = '2onif3d-9439ffdw-md2093fn2-0394vncwpm9423fv'

            if 'hub.mode' in request.args:
                mode = request.args.get('hub.mode')
                print(mode)
            if 'hub.verify_token' in request.args:
                token = request.args.get('hub.verify_token')
                print(f"this is the normal token {token}")
                print(token)
            if 'hub.challenge' in request.args:
                challenge = request.args.get('hub.challenge')
                print(challenge)
            if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
                mode = request.args.get('hub.mode')
                token = request.args.get('hub.verify_token')
                print(f"this is the and statment token {token}")

                if mode == 'subscribe' and token == VERIFY_TOKEN:

                    print("WEBHOOK VERIFIED")

                    challenge = request.args.get('hub.challenge')

                    return challenge, 200

                else:
                    return 'ERROR', 403

            data = request.data
            dataOBJ = json.loads(data.decode('utf-8'))

            print(f"Data object is {dataOBJ}")
            if 'object' in dataOBJ and dataOBJ['object'] == 'page':
                
                print(dataOBJ)
                entries = dataOBJ['entry']
                for entry in entries:
                    webhookEvent = entry['messaging'][0]
                    print(webhookEvent)

                    senderPsid = webhookEvent['sender']['id']
                    print(f"Sender PSID is {senderPsid}")

                    if 'message' in webhookEvent:
                        handleMessage(senderPsid, webhookEvent['message'])

                        return 'EVENT_RECEIVED', 200
                    if 'postback' in webhookEvent:

                        payload_user = webhookEvent['postback']['payload']
                        postbackHandler(senderPsid, payload_user)
                        return 'EVENT_RECIVED', 200
                    else:
                        return 'ERROR', 404


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8888, debug=True)