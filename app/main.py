import webservice
import plugins
import bottle
import reply
import sys

bottle.BaseResponse.default_content_type = 'application/json; charset=UTF-8'
bottle.ERROR_PAGE_TEMPLATE = str(reply.build(False, None))

URI_PARTS = {'name': '<name:re:[a-zA-Z]{6,24}>'}

def route(uri, func, method='GET'):
    return [uri.format(**URI_PARTS), func, method]

URI_MAP = [route('/', webservice.ws),
           route('/hello/{name}', webservice.ws_hello)]

APP = bottle.app()

for uri, func, method in URI_MAP:
    APP.route(uri, method=method, apply=[plugins.PreRequest])(func)

if __name__ == '__main__':
    bottle.run(APP, server='wsgiref', port=9000, host='0.0.0.0')

# EOF
