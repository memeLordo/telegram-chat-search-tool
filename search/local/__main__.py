from .commands import start_search
from .errors import (eof_handler, id_error_handler, keyinterrupt_handler,
                     unknown_handler)


@unknown_handler
@keyinterrupt_handler
@eof_handler
@id_error_handler
def main():
    start_search()


if __name__ == "__main__":
    main()
    input("Нажмите любую клавишу для завершения...")
