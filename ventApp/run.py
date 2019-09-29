from flask import Flask, request, redirect
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
from models import *

knownIllnesses = {"anxiety":["Bernstein", "+19457743030"], "depression": ["Hammock", "+12229058989"], "bipolar":["Hawk", "+12229057989"]}
                # "post traumatic stresss disorder", "substance abuse", "delirium",
                # "phobia", "self harm", "suicide", "Schiztophrenia"}


app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None).lower().strip()
    resp = MessagingResponse()

    if body in knownIllnesses.keys():
        resp.message("Thank you for sharing your issues with " + body + ". According to our records, Dr. " + knownIllnesses[body][0] + " will be able to help you appropriately.\
        Please reach out to him now through this direct number: " + knownIllnesses[body][1])
    elif body == 'bye':
        resp.message("Goodbye")
    elif body == 'help me':
        resp.message("Please list one or more disorders or symptoms of disoreders of which you suffer \
        and we will link you with an appropritate specialist. e.g. text 'Depression' OR text 'bye' to terminate\
        this session.")
    else:
        resp.message("Type 'Help me' for help, ")

    return str(resp)

Bot = VentUser("Bot", "+19142523220", "AC499820668088575e6867dc060ba42ec9", "03e14d687eb5ce09de59772e06c292ed")
runner = Twilio(Bot)


if __name__ == "__main__":
    app.run(debug=True)
