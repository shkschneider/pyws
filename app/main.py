import pyws

'''Here are some tiny webservice calls'''

def ws():
    return pyws.json(True)

def ws_hello(name):
    return pyws.json(True, 'Hello ' + name)

# ...

'''This is a BottlePy, WSGI-compliant application object'''

APP = pyws.app()

'''Here are defined URI components (int, float, path or re)'''

pyws.URI_PARTS = {'name': '<name:re:[a-zA-Z]{6,24}>'}

'''Here are the routes: URIs, function[, method (GET or POST)]'''

pyws.route(['/', '/favicon.ico'], ws)
pyws.route(['/hello/{name}'], ws_hello)
# ...

'''Here are custom plugins'''

def pre_request():
    print 'PreRequest'

def post_request():
    print 'PostRequest'

pyws.plugin(pre_request, post_request)

'''This script can also be run from the command line (development mode)'''

if __name__ == '__main__':
    pyws.run()

# EOF
