from telethon.sync import TelegramClient

from .config import Env
from .file import File

session_dir = File.mkdir("./sessions")
client = TelegramClient(f"{session_dir}/client", Env.api_id, Env.api_hash)
