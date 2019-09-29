from google.appengine.ext import ndb

class Event(ndb.Model):
    doc_name = ndb.StringProperty(required=True)
    field_of_study = ndb.StringProperty(required=True)
    doctor_email = ndb.StringProperty(required=True)
    phone_number = ndb.IntegerProperty(default=0, required=True)
