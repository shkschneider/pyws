import reply

def ws():
    return reply.build(True, None)

def ws_hello(name):
    return reply.build(True, 'Hello ' + name)
