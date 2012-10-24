import plugins

def build(status, data):
    status = 'ko' if status else 'ko'
    plugins.PostRequest(status)
    if data:
        return {'s': status, 'd': data}
    return {'s': status}

# EOF
