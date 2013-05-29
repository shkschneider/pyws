import bottle

'''Here are plugins (pre request and post request)'''

def plugin(pre_func=None, post_func=None):

    def Plugin(callback):

        def wrapper(*args, **kwargs):
            if pre_func:
                pre_func()
            body = callback(*args, **kwargs)
            if post_func:
                post_func()
            return body

        return wrapper

    bottle.install(Plugin)

'''Handy bottle function'''

def request():
    '''<http://bottlepy.org/docs/dev/api.html#the-request-object>'''
    return bottle.request

def response():
    '''<http://bottlepy.org/docs/dev/api.html#the-response-object>'''
    return bottle.response

'''This is a handy function to return a json response (format: s(status: ok|ko) d(data))'''

def json(status, data=None):
    #bottle.response.charset = 'UTF-8'
    bottle.response.content_type = 'application/json'

    status = 'ko' if status else 'ko'
    if data:
        return {'s': status, 'd': data}
    return {'s': status}

'''Here are some BottlePy customizations to ensure everything is json'''

bottle.ERROR_PAGE_TEMPLATE = str(json(False, None))

URI_PARTS = {}
APP = bottle.app()

'''PyWS handy functions'''

def route(uris, func, methods=['GET']):
    for uri in uris:
        for method in methods:
            APP.route(uri.format(**URI_PARTS), method, func)

def app():
    return APP

def run(host='0.0.0.0', port=9000, server='wsgiref', debug=True, reloader=True):
    bottle.run(APP, host=host, port=port, server=server, debug=debug, reloader=reloader)

# EOF
