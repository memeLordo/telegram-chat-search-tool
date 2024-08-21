import os
import sys
import time

from dotenv import dotenv_values, set_key
from telethon.errors.rpcerrorlist import ApiIdInvalidError, HashInvalidError
from telethon.sync import TelegramClient

symbols = "-" * 50
loading = f"Loading: [{symbols}]"
backtrack = "\b" * len(loading)


def mkdir(dirname: str):
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


def get_env_keys():
    try:
        env_config = dotenv_values(".env.script")
        api_id = int(env_config["API_ID"] or 0)
        api_hash = str(env_config["API_HASH"] or None)
        return (api_id, api_hash)
    except KeyError:
        return set_env_keys()


def set_env_keys():
    try:
        api_id = int(input("API_ID: "))
        api_hash = input("API_HASH: ")
        set_key(".env.script", "API_ID", str(api_id))
        set_key(".env.script", "API_HASH", api_hash)
        return (api_id, api_hash)
    except ValueError:
        print("IP должно быть числом!")
        return set_env_keys()


async def search():
    global client, loading, symbols
    _loading = loading
    request = input("Введите ключ поиска: ")
    result = f'Результаты по запросу "{request}":'
    dialogs = await client.get_dialogs()

    delta = len(symbols) / len(dialogs)
    _delta = 1 / delta

    sys.stdout.write(backtrack + _loading)
    for i, dialog in enumerate(dialogs, len(dialogs) + 1):
        if dialog.is_group or dialog.is_channel:
            async for _ in client.iter_messages(
                dialog,
                search=request,
                limit=100,
            ):
                result = result + "\n" + dialog.name
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


def start_client(api_id, api_hash):
    def run_():
        with client:
            result = client.loop.run_until_complete(search())
        match input("Сохранить результат в файл (y/N): "):
            case "y":
                save_to_txt(result)
                print("<End message>")

    global client
    session_dir = mkdir("./sessions")
    client = TelegramClient(f"{session_dir}/client", api_id, api_hash)
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


if __name__ == "__main__":
    main()
