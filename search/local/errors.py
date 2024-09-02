from telethon.errors.rpcerrorlist import ApiIdInvalidError, HashInvalidError

from .config import Env


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


id_error_handler = error_handler(
    errors=(ApiIdInvalidError, HashInvalidError),
    err_message="Данные введены неверно.",
    callable=True,
    custom_func=Env.set_keys,
)
eof_handler = error_handler(EOFError, "Превышено время ожидания. Перезапуск программы.")
keyinterrupt_handler = error_handler(KeyboardInterrupt, "Выход из программы.")
