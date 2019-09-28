# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models import *

Bot = VentUser("Bot", "+13343669908", "AC8024f910a1dc56ecd5f04b72addce327", "5d8d4bb721c5e4161ea439765a90418d")
Runner = Twilio(Bot)
Runner.createMessage("+12017232117", "ayo bish")

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
