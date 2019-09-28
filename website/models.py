from google.appengine.ext import ndb

class Event(ndb.Model):
    host_name = ndb.StringProperty()
    field_of_study = ndb.StringProperty()
    doctor_short_description = ndb.TextProperty()
    doctor_email = ndb.StringProperty()
    phone_number = ndb.IntegerProperty(default=0)
