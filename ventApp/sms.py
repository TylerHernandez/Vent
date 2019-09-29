from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models import *
from twilio.rest import Client

account_sid = 'AC499820668088575e6867dc060ba42ec9'
auth_token = '03e14d687eb5ce09de59772e06c292ed'
client = Client(account_sid, auth_token)
message = client.messages.create(
 body='This is a test message!',
 from_='[+][1][9142523220]',
 to='[+][1][9146203493]'
 )
