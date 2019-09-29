from google.appengine.ext import ndb

class Event(ndb.Model):
    doc_name = ndb.StringProperty(required=True)
    field_of_study = ndb.StringProperty(required=True)
    doctor_email = ndb.StringProperty(required=True)
    phone_number = ndb.IntegerProperty(default=0, required=True)
Bill = Event (doc_name="Bill Smith", field_of_study = "Death", doctor_email = "Test@test.com", phone_number = 1234567890)
Bill.put()
