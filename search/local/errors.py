def error_handler(errors=(Exception,), err_message=" "):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)

            except errors as e:
                return func(*args, **kwargs)

        return wrapped

    return wrapper
