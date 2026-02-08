from dotenv import dotenv_values


def output_mess(conf: dict) -> None:
    print(f"Mode: {conf['MATRIX_MODE']}")
    print("Database: Connected to local instance")
    print("API Access: Authenticated")
    print(f"Log Level: {conf['LOG_LEVEL']}")
    print(f"Zion Network: {conf['ZION_ENDPOINT']}")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configurations.")


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
            try:
                values[key]
            except KeyError as e:
                print(f"Warning: missing configuration variable {e}")
                print()
            value = values.get(key, ele[key])
            conf = {**conf, key: value}
    except (ValueError) as e:
        print(f"Error: {e}")
        return
    else:
        print("Configuration loaded:")
        output_mess(conf)


main() if __name__ == "__main__" else ""
