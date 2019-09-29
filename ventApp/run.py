from flask import Flask, request
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from models import *

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming calls with a MMS message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a text message
    msg = resp.message("The Robots are coming! Head for the hills!")

    # Add a picture message
    msg.media("https://farm8.staticflickr.com/7090/6941316406_80b4d6d50e_z_d.jpg")

    return str(resp)

Bot = VentUser("Bot", "+19142523220", "AC499820668088575e6867dc060ba42ec9", "03e14d687eb5ce09de59772e06c292ed")
runner = Twilio(Bot)

while True:
    if runner.giveLastestmsg().body == "penis":
        print(runner.giveLastestmsg().body)
        break

if __name__ == "__main__":
    app.run(debug=True)
