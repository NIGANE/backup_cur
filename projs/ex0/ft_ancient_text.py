
def ft_ancient_text(file_name: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print("")

    try:
        print(f"Accessing Storage Vault: {file_name}")
        data = open(file_name, "r")
        if (data is False):
            print("Error")
            return
    except FileNotFoundError as e:
        print(e)
    else:
        print("Connection established...")
        print("")
        print(data.read())
        data.close()
    finally:
        print("")
        print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    ft_ancient_text("ancient_fragment.txt")
