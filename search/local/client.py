from telethon.sync import TelegramClient


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
