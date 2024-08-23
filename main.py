import os
import sys
import time

from dotenv import dotenv_values, set_key
from telethon.errors.rpcerrorlist import ApiIdInvalidError, HashInvalidError
from telethon.sync import TelegramClient
from telethon.tl.custom import Dialog

# TODO: Make Loading class
symbols = "-" * 50
loading = f"Loading: [{symbols}]"
backtrack = "\b" * len(loading)


def mkdir(dirname: str) -> str:
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return dirname


def save_to_txt(text: str):
    global index
    dir = mkdir("./requests")
    filename = f"{dir}/request[{index}].txt"
    while os.path.exists(filename):
        index += 1
        filename = f"{dir}/request[{index}].txt"
    with open(filename, "w+") as file:
        file.write(text)
    index += 1
    print("Файл сохранён.")


def set_env_keys() -> tuple[int, str]:
    try:
        api_id = int(input("API_ID: "))
        api_hash = input("API_HASH: ")
        set_key(".env.script", "API_ID", str(api_id))
        set_key(".env.script", "API_HASH", api_hash)
        return (api_id, api_hash)
    except ValueError:
        print("IP должно быть числом!")
        return set_env_keys()


# TODO: Make mode class
def get_mode_from(env_config: dict[str, str | None]):
    try:
        global mode
        mode = str(env_config["MODE"])
        if str(mode).lower() not in ("title", "link"):
            raise KeyError
    except KeyError:
        _, _, mode = set_key(".env.script", "MODE", "link")
    print(f"Установлен режим вывода {repr(mode).upper()}")


def get_env_keys() -> tuple[int, str]:
    try:
        env_config = dotenv_values(".env.script")
        get_mode_from(env_config)
        api_id = int(env_config["API_ID"] or 0)
        api_hash = str(env_config["API_HASH"] or None)
        return (api_id, api_hash)
    except KeyError:
        return set_env_keys()


def set_message(text: str, dialog: Dialog):
    global mode
    match str(mode).lower():
        case "link":
            try:
                if dialog.entity.username is None:
                    raise AttributeError
                return text + "\nhttps://t.me/" + dialog.entity.username
            except AttributeError:
                return text
        case _:
            return text + "\n" + dialog.title


async def search() -> str:
    global client, loading, symbols
    _loading = loading
    request: str = input("Поиск: ")
    result: str = f'Результаты по запросу "{request}":'
    dialogs = await client.get_dialogs()

    delta = len(symbols) / len(dialogs)
    _delta = 1 / delta

    sys.stdout.write(backtrack + _loading)
    for i, dialog in enumerate(dialogs, len(dialogs) + 1):
        if dialog.is_group or dialog.is_channel:
            async for _ in client.iter_messages(
                entity=dialog,
                search=request,
                limit=100,
            ):
                result = set_message(result, dialog)
                break

        if i % _delta * delta >= 1 - delta:
            _loading = _loading.replace(symbols[0], "=", 1)
            sys.stdout.flush()
            sys.stdout.write(backtrack + _loading)
            time.sleep(1 / len(symbols))
    sys.stdout.write(backtrack)
    print("Complete!" + " " * len(_loading), end="\n")
    print(symbols + "\n" + result + "\n" + symbols, end="\n")
    return result


def start_client(api_id: int, api_hash: str):
    def run_():
        with client:
            result = client.loop.run_until_complete(search())
        match input("Сохранить результат в файл (y/N): "):
            case "y":
                mode_stat = f"MODE: {str(mode).upper()}\n"
                save_to_txt(mode_stat + result)
            case _:
                pass

    global client
    session_dir = mkdir("./sessions")
    client = TelegramClient(f"{session_dir}/client", api_id, api_hash)
    while True:
        run_()


def main():
    try:
        global index
        index = 1
        api_id, api_hash = get_env_keys()
        start_client(api_id, api_hash)
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
