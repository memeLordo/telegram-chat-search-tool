def error_handler(errors=(Exception,), err_message=" ", callable=True):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors:
                print(err_message)
                if callable:
                    return func(*args, **kwargs)

        return wrapped

    return wrapper
