from dotenv import dotenv_values, set_key


def get_env_keys():
    try:
        env_config = dotenv_values(".env.script")
        api_id = env_config["API_ID"]
        api_hash = env_config["API_HASH"]
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


def main():
    api_id, api_hash = get_env_keys()
    print(api_id, api_hash, end="\n")


if __name__ == "__main__":
    main()
