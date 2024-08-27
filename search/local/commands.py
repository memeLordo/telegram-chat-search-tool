import sys
import time

from telethon.tl.custom import Dialog

from .client import client
from .config import Env
from .loading import Load


def set_message(text: str, dialog: Dialog):
    match Env.mode.lower():
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
    global client
    loading = Load.message
    backtrack = Load.backtrack
    bar = Load.bar
    request: str = input("Поиск: ")
    result: str = f'Результаты по запросу "{request}":'
    dialogs = await client.get_dialogs()

    delta = bar.length / len(dialogs)
    _delta = 1 / delta

    sys.stdout.write(backtrack + loading)
    for i, dialog in enumerate(dialogs, len(dialogs) + 1):
        if len(dialogs) > 1000:
            time.sleep(0.6)
        if dialog.is_group or dialog.is_channel:
            async for _ in client.iter_messages(
                entity=dialog,
                search=request,
                limit=100,
            ):
                result = set_message(result, dialog)
                break

        if i % _delta * delta >= 1 - delta:
            loading = loading.replace(bar.symbol, "=", 1)
            sys.stdout.flush()
            sys.stdout.write(backtrack + loading)
            time.sleep(1 / bar.length)
    sys.stdout.write(backtrack + "Complete!" + len(backtrack) * " ")
    print(f"\n{bar}\n{result}\n{bar}\n")
    return result
