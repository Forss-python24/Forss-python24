import Messenger_botV1
from flask import Flask, request
import json

bot = Messenger_botV1.Messenger_bot()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'FOI2F-R24F9-NC234-DP94R'

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
                    bot.handleMessage(senderPsid, webhookEvent['message'])

                    return 'EVENT_RECEIVED', 200
                else:
                    return 'ERROR', 404


if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8888, debug=True)