import webservice
import pyws
import sys

APP = pyws.app()

pyws.URI_PARTS = {'name': '<name:re:[a-zA-Z]{6,24}>'}
pyws.route(['/', '/favicon.ico'], webservice.ws)
pyws.route(['/hello/{name}'], webservice.ws_hello)

if __name__ == '__main__':
    pyws.run(host='0.0.0.0', port=9000)

# EOF
