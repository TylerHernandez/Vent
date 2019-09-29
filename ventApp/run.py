# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from models import *


Bot = VentUser("Bot", "+19142523220", "AC499820668088575e6867dc060ba42ec9", "03e14d687eb5ce09de59772e06c292ed")
runner = Twilio(Bot)

while True:
    if runner.giveLastestmsg().body == "penis":
        print(runner.giveLastestmsg().body)
        break



app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    message= Message()
    message.body("Ahoy! Thanks so much for your message.")
    resp.append(message)

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
