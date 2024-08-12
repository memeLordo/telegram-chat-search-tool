from dotenv import dotenv_values, set_key


def get_env_keys():
    try:
        env_config = dotenv_values(".env.script")
        api_id = env_config["BOT_ID"]
        api_hash = env_config["BOT_HASH"]
    except KeyError:
        api_id = input("API_ID: ")
        api_hash = input("API_HASH: ")
        set_key(".env.script", "API_ID", api_id)
        set_key(".env.script", "API_HASH", api_hash)
    return (api_id, api_hash)


def main():
    api_id, api_hash = get_env_keys()
    print(api_id, api_hash, end="\n")


if __name__ == "__main__":
    main()
