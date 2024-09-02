from enum import Enum

from dotenv import dotenv_values, set_key


class Mode(Enum):
    LINK = "link"
    TIITLE = "title"

    @classmethod
    def find(cls, param):
        for e in Mode:
            if e.value == param:
                return e
        raise KeyError


class Env:
    __file__ = ".env.config"

    @classmethod
    def create(cls):
        try:
            env_config = dotenv_values(cls.__file__)
            cls.get_mode_from(env_config)
            cls.api_id = int(env_config["API_ID"] or 0)
            cls.api_hash = str(env_config["API_HASH"] or None)
        except KeyError:
            cls.set_keys()

    @classmethod
    def get_mode_from(cls, env_config: dict[str, str | None]):
        try:
            cls.mode = str(env_config["MODE"])
            if str(cls.mode).lower() not in ("title", "link"):
                raise KeyError
        except KeyError:
            _, _, cls.mode = set_key(cls.__file__, "MODE", "link")

    @classmethod
    def set_keys(cls):
        try:
            cls.api_id = int(input("API_ID: "))
            cls.api_hash = input("API_HASH: ")
            set_key(cls.__file__, "API_ID", str(cls.api_id))
            set_key(cls.__file__, "API_HASH", cls.api_hash)
        except ValueError:
            print("IP должно быть числом!")
            return cls.set_keys()

    @classmethod
    def _mode(cls) -> str:
        return f"MODE: {cls.mode.upper()}\n"

    @classmethod
    def _output(cls) -> str:
        return f"Установлен режим вывода {cls.mode.upper()}"
