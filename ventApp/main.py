from twilio.rest import Client
from models import *

account_sid = "AC499820668088575e6867dc060ba42ec9"

auth_token  = "03e14d687eb5ce09de59772e06c292ed"


client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+1(914)620-3493",
    from_="+1(914)252-3220",#from_="+1(914)252-3220",
    body="WHAT IT DO BABYYYYY")

print(message.sid)



#n = name of user that just send text
ammar = VentUser("Ammar", "9146203493")

print(ammar)
# string[][] information_list = new string[][];
# dictionary
# for(int i=0; i<information_list.length; i++)
# {
# // categories
#     for(int x=0; x<information_list[i].length; x++)
#     {
#     dictionary.append { doc, patient }
#     }
# }
#
# array list 2d of category
#
#     {key: doctor,
#     value: patients}
