import sys

from telethon.errors.rpcerrorlist import ApiIdInvalidError, HashInvalidError

from .client import start_search

def main():
    try:
        global index
        index = 1
        api_id, api_hash = get_env_keys()
        start_search()
    except EOFError:
        print("Превышено время ожидания. Перезапуск программы.")
        main()
    except (ApiIdInvalidError, HashInvalidError):
        print("Данные введены неверно. Повторите попытку.")
        main()
    except KeyboardInterrupt:
        print("\nВыход из программы.")
    except Exception as e:
        print("Unhandled error!", file=sys.stderr, flush=True)
        print(f"\n{repr(e)}")


if __name__ == "__main__":
    main()
    input("Нажмите любую клавишу для завершения...")
