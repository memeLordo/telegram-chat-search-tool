def error_handler(
    errors=(Exception,),
    err_message="Unhandled error!",
    callable=False,
    custom_func=lambda: None,
):
    def wrapper(func):
        def wrapped(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except errors as e:
                print("\n" + err_message)
                if errors == (Exception,):
                    print(repr(e))
                custom_func()
            finally:
                if callable:
                    return func(*args, **kwargs)

        return wrapped

    return wrapper
