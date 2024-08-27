from dotenv import dotenv_values, set_key


class Env:
    __file__ = ".env.config"

    @classmethod
    def get_mode_from(cls, env_config: dict[str, str | None]):
        try:
            cls.mode = str(env_config["MODE"])
            if str(cls.mode).lower() not in ("title", "link"):
                raise KeyError
        except KeyError:
            _, _, cls.mode = set_key(cls.__file__, "MODE", "link")

    @classmethod
    def set_keys(cls) -> tuple[int, str]:
        try:
            cls.api_id = int(input("API_ID: "))
            cls.api_hash = input("API_HASH: ")
            set_key(cls.__file__, "API_ID", str(cls.api_id))
            set_key(cls.__file__, "API_HASH", cls.api_hash)
            return (cls.api_id, cls.api_hash)
        except ValueError:
            print("IP должно быть числом!")
            return cls.set_keys()

    @classmethod
    def get_keys(cls) -> tuple[int, str]:
        try:
            env_config = dotenv_values(".env.config")
            cls.get_mode_from(env_config)
            api_id = int(env_config["API_ID"] or 0)
            api_hash = str(env_config["API_HASH"] or None)
            return (api_id, api_hash)
        except KeyError:
            return cls.set_keys()

        # print(f"Установлен режим вывода {repr(mode).upper()}")
