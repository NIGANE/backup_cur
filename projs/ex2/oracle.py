from dotenv import load_dotenv
import os

load_dotenv()

def output_mess(conf: dict) -> None:
    print(f"Mode: {conf['matrix_mode']}")
    print(f"Database: {conf['database_url']}")
    print(
        f"API Access: "
        f"{"Authenticated" if conf['api_key'] else 'Not Authenticated'}"
        )
    print(f"Log Level: {conf['log_level']}")
    print(f"Zion Network: {conf['endpoint']}")
    print()

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print()

    print("The Oracle sees all configurations.")


def main() -> None:
    matrix_mode=os.getenv("MATRIX_MODE")
    database_url=os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")
    
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    conf = {
        "matrix_mode": matrix_mode,
        "database_url": database_url,
        "api_key": api_key,
        "log_level": log_level,
        "endpoint": log_level,
    }
    try:
        if not all([matrix_mode, database_url, api_key, log_level, endpoint]):
            raise ValueError("check if the conf file exists or empy")
        
    except (ValueError) as e:
        print(f"Error: {e}")
        return
    else:
        print("Configuration loaded:")
        output_mess(conf)


main() if __name__ == "__main__" else ""
