def PreRequest(callback):

    def wrapper(*args, **kwargs):
        # ...

        body = callback(*args, **kwargs)
        return body

    return wrapper

def PostRequest(status):
    # ...

    return

# EOF
