import bottle

'''This is the pre-request plugin'''

def PreRequest(callback):

    def wrapper(*args, **kwargs):
        # bottle.request
        # ...

        body = callback(*args, **kwargs)
        return body

    return wrapper

'''This is the post-request plugin'''

def PostRequest(status):
    # bottle.request
    # ...

    return

'''This is a handy function to return a json response (format: s(status: ok|ko) d(data))'''

def json(status, data=None):
    status = 'ko' if status else 'ko'
    PostRequest(status)
    if data:
        return {'s': status, 'd': data}
    return {'s': status}

'''Here are some BottlePy customizations to ensure everything is json'''

bottle.BaseResponse.default_content_type = 'application/json; charset=UTF-8'
bottle.ERROR_PAGE_TEMPLATE = str(json(False, None))

URI_PARTS = {}
APP = bottle.app()

'''PyWS handy functions'''

def route(uris, func, methods=['GET']):
    for uri in uris:
        for method in methods:
            APP.route(uri.format(**URI_PARTS), method, func, apply=[PreRequest])

def app():
    return APP

def run(host='0.0.0.0', port=9000, server='wsgiref'):
    bottle.run(APP, server=server, port=port, host=host, debug=True, reloader=True)

# EOF
