import webapp2
from google.appengine.ext import ndb
from models import Event
import jinja2
import os


jinja_enviroment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Submit(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/submit.html")

        self.response.write(template.render())

class Number(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/number.html")

        self.response.write(template.render())

class IntroPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_enviroment.get_template("/templates/index.html")

        self.response.write(template.render())

    def post(self):
        results_template = jinja_enviroment.get_template('./templates/index.html')
        event_post ={

        "doc_name" : self.request.get("doc_name"),
        "field_of_study" : self.request.get("field_of_study"),
        "doctor_email" : self.request.get("doctor_email"),
        "phone_number" : self.request.get("phone_number")
        }

        # event_post = Event(doc_name=doc_name,
        #          doctor_email=doctor_email,
        #          field_of_study=field_of_study,
        #          phone_number=phone_number)
        event_post.put()
        self.response.write(results_template.render(event_post))

app = webapp2.WSGIApplication([
    ('/', IntroPage),
    ('/submit', Submit),
    ('/number', Number),

], debug=True)
