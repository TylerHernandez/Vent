from twilio.rest import Client
class Twilio:
    def __init__(self, user):
        self.user = user
        self.account_sid = user.account_sid
        self.auth_token = user.auth_token
        self.client = Client(self.account_sid, self.auth_token)

    def giveLastestmsg(self):
        messages = self.client.messages.list(limit=20)
        return messages[0]

    def createMessage(self, toWho, whatURL):
        call = self.client.messages.create(
        to=toWho,
        from_=self.user.phoneNumber,
        body=whatURL
        )
        print(call.sid)

class VentUser:

    def __init__(self, name, phoneNumber, account_sid, auth_token):
        self.name = name
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.phoneNumber = phoneNumber
        self.diseases = []
        self.doctors = []

    def __str__(self ):
        str = self.name + " " + self.phoneNumber + "\ndiseases: "
        if len(diseases) > 0:
            for di in diseases:
                str += i
        if len(doctors) > 0:
            str += "\nDoctors: "
            for doc in doctors:
                str += doc
        return str

    def addDisease(self, disease):
        diseases.apend(disease)

    def addDoctor(self, doc):
        doctors.append(doc)
