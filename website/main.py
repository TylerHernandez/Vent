import webapp2
from google.appengine.ext import ndb


import jinja2
import os


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class IntroPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/index.html")

        self.response.write(template.render(template_vars))

    def post(self):
        template = jinja_env.get_template('/templates/index.html')


class GiveHelpPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = jinja_env.get_template("/templates/givehelp.html")

        self.response.write(template.render(template_vars))

    def post(self):
        template = jinja_env.get_template('/templates/givehelp.html')










app = webapp2.WSGIApplication([
    ('/', IntroPage),
    ('/givehelp', GiveHelpPage),

], debug=True)
