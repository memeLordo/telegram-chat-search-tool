from dotenv import dotenv_values
def main():
    env_config = dotenv_values(".env.script")
    api_id = env_config["BOT_ID"]
    api_hash = env_config["BOT_HASH"]
    print(api_id, api_hash, end="\n")
if __name__ == "__main__":
    main()
