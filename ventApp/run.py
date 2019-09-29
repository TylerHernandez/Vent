from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from models import *

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    resp = MessagingResponse()
    print(body)

    if body == 'hello':
        resp.message("Hi!")
    elif body == 'bye':
        resp.message("Goodbye")

    return str(resp)

Bot = VentUser("Bot", "+19142523220", "AC499820668088575e6867dc060ba42ec9", "03e14d687eb5ce09de59772e06c292ed")
runner = Twilio(Bot)


if __name__ == "__main__":
    app.run(debug=True)
