import bottle

def PreRequest(callback):

    def wrapper(*args, **kwargs):
        # ...

        body = callback(*args, **kwargs)
        return body

    return wrapper

def PostRequest(status):
    # ...

    return

def json(status, data=None):
    status = 'ko' if status else 'ko'
    PostRequest(status)
    if data:
        return {'s': status, 'd': data}
    return {'s': status}

bottle.BaseResponse.default_content_type = 'application/json; charset=UTF-8'
bottle.ERROR_PAGE_TEMPLATE = str(json(False, None))

# :int :float :path :re:exp
URI_PARTS = {}

APP = bottle.app()

# HEAD GET POST
def route(uris, func, methods=['GET']):
    for uri in uris:
        for method in methods:
            APP.route(uri.format(**URI_PARTS), method, func, apply=[PreRequest])

def app():
    return APP

def run(host='0.0.0.0', port=9000, server='wsgiref'):
    bottle.run(APP, server=server, port=port, host=host, debug=True, reloader=True)

# EOF
