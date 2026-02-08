from dotenv import load_dotenv, dotenv_values


def output_mess(conf: dict) -> None:
    print(conf)
    print(f"Mode: {conf['MATRIX_MODE']}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {conf['LOG_LEVEL']}")
    print(f"Zion Network: {conf['ZION_ENDPOINT']}")
    print()

    print("Environment security check:")


def main() -> None:
    values = dotenv_values(".env")
    targets = [
        {
            'MATRIX_MODE': "default Mode"
            },
        {
            'DATABASE_URL': "default url"
            },
        {
            'API_KEY': "default key"
            },
        {
            'LOG_LEVEL': "default log"
            },
        {
            'ZION_ENDPOINT': "default endpoint"
            }
        ]

    print("ORACLE STATUS: Reading the Matrix...")
    print()
    conf = {}
    try:
        if (len(values)) == 0:
            raise ValueError("check if the conf file exists or empy")
        for ele in targets:
            key = [*ele.keys()][0]
            value = values.get(key, ele[key])
            conf = {**conf, key: value}
    except (KeyError, ValueError) as e:
        print(f"Warning: missing configuration variable :{e}")
    else:
        print("Configuration loaded:")
        output_mess(conf)


main() if __name__ == "__main__" else ""
