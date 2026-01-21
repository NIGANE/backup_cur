
def read_data(file_name: str) -> None:
    try:
        print("Inscribing preservation data...")
        data = open(file_name, "r")
        if (data is False):
            print("Error")
            return
    except FileNotFoundError as e:
        print(e)
    else:
        print(data.read())
        data.close()


def ft_archive_creation(file_name: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print("")
    try:
        print(f"Initializing new storage unit: {file_name}")
        file = open(file_name, "w")
    except (Exception) as e:
        print(e)
    else:
        file.write("[ENTRY 001] New quantum algorithm discovered\n")
        file.write("[ENTRY 002] Efficiency increased by 347%\n")
        file.write("[ENTRY 003] Archived by Data Archivist trainee")
        print("Storage unit created successfully...")
        print("")
        file.close()
        read_data(file_name)
        print("")
        print("Data inscription complete. Storage unit sealed.")
        print(f"Archive '{file_name}' ready for long-term preservation.")


if __name__ == "__main__":
    ft_archive_creation("new_discovery.txt")
