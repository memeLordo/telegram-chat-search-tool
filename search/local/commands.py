import time

from telethon.tl.custom import Dialog

from search.local.loading import Load


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
    global client
    _loading = Load.message
    request: str = input("Поиск: ")
    result: str = f'Результаты по запросу "{request}":'
    dialogs = await client.get_dialogs()

    delta = len(symbols) / len(dialogs)
    _delta = 1 / delta

    sys.stdout.write(backtrack + _loading)
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
            _loading = _loading.replace(symbols[0], "=", 1)
            sys.stdout.flush()
            sys.stdout.write(backtrack + _loading)
            time.sleep(1 / len(symbols))
    sys.stdout.write(backtrack)
    print("Complete!" + " " * len(_loading), end="\n")
    print(symbols + "\n" + result + "\n" + symbols, end="\n")
    return result
