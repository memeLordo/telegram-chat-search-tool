from telethon.sync import TelegramClient

from .commands import search
from .config import Env
from .file import File

session_dir = File.mkdir("./sessions")
client = TelegramClient(f"{session_dir}/client", Env.api_id, Env.api_hash)


def start_search():
    def run_():
        with client:
            result = client.loop.run_until_complete(search())
        match input("Сохранить результат в файл (y/N): "):
            case "y":
                mode_stat = f"MODE: {str(mode).upper()}\n"
                save_to_txt(mode_stat + result)
            case _:
                pass

    while True:
        run_()
