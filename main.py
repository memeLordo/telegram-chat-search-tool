from dotenv import dotenv_values, set_key
from telethon import TelegramClient
from telethon.errors.rpcerrorlist import ApiIdInvalidError, HashInvalidError


def save_to_txt(text: str):
    global index
    filename = f"./requests/request{index}.txt"
    filename = f"{dir}/request{index}.txt"
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


async def search(request: str):
    global client
    result = ""
    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel:
            async for user in client.iter_messages(
                dialog,
                search=request,
                limit=100,
            ):  # TODO: rewrite for next const as for loop is unused
                result = result + "\n" + dialog.name
                break
    return result


def start_client(api_id, api_hash):
    def run_():
        global client
        search_request = input("Введите ключ поиска: ")
        with client:
            return client.loop.run_until_complete(search(search_request))

    try:
        global client
        client = TelegramClient("./sessions/client", api_id, api_hash)
        result = run_()
        save_file = input("Сохранить результат в файл (y/N): ")
        match save_file:
            case "y":
                save_to_txt(result)
        print("<End message>")
    except (ApiIdInvalidError, HashInvalidError):
        print("Данные введены неверно. Повторите попытку.")
        api_id, api_hash = set_env_keys()
        start_client(api_id, api_hash)


def main():
    global index
    index = 1
    api_id, api_hash = get_env_keys()
    start_client(api_id, api_hash)


if __name__ == "__main__":
    main()
