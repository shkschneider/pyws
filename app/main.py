import webservice
import plugins
import bottle
import reply
import sys

bottle.BaseResponse.default_content_type = 'application/json; charset=UTF-8'
bottle.ERROR_PAGE_TEMPLATE = str(reply.build(False, None))

APP = bottle.app()

# :int :float :path :re:exp
URI_PARTS = {'name': '<name:re:[a-zA-Z]{6,24}>'}

# HEAD GET POST
def route(uris, func, methods=['GET']):
    for uri in uris:
        for method in methods:
            APP.route(uri.format(**URI_PARTS), method, func)

route(['/'], webservice.ws)
route(['/hello/{name}'], webservice.ws_hello)

if __name__ == '__main__':
    bottle.run(APP, server='wsgiref', port=9000, host='0.0.0.0', debug=True, reloader=True)

# EOF
