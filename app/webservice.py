import pyws

def ws():
    return pyws.json(True)

def ws_hello(name):
    return pyws.json(True, 'Hello ' + name)
