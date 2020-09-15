import cherrypy, socket, os
from os import urandom
from hashlib import pbkdf2_hmac
from cherrypy.lib.static import serve_file
import json

ROOT = os.path.abspath(os.getcwd())
print(ROOT)

class WebApp():

    @cherrypy.expose
    def index(self):
        return serve_file(os.path.join('C:\\Users\\Niko\\OneDrive - ECAM\\ECAM\\BA2\\Q2\\GitHub\\ECAM\\2BA\\Informatic\\TP\\TP 4 Network\\index.htm'))

    @cherrypy.expose
    def default(self, attr='abc'):
        return serve_file(os.path.join('C:\\Users\\Niko\\OneDrive - ECAM\\ECAM\\BA2\\Q2\\GitHub\\ECAM\\2BA\\Informatic\\TP\\TP 4 Network\\errorr.htm'))

    @cherrypy.expose
    def signUp(self):
        return serve_file(os.path.join('C:\\Users\\Niko\\OneDrive - ECAM\\ECAM\\BA2\\Q2\\GitHub\\ECAM\\2BA\\Informatic\\TP\\TP 4 Network\\signup.html'))
    
    @cherrypy.expose
    def signIn(self, name):
        return 'You can now sign in {} !'.format(name)

    @cherrypy.expose
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    def adduser(self):
        data = cherrypy.request.json
        user = json.loads(data)
        print('>Ajout de ' + user['name'])
        return {'OK': True}

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def listusers(self):
        return serve_file(os.path.join(ROOT, 'listusers.htm'))

cherrypy.quickstart(WebApp(), '', ROOT + '\\2BA\\Informatic\\TP\\TP 4 Network\\server.conf')
