def ft_crisis_response(file_name: str) -> None:

    try:
        with open(file_name) as f:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            print(f"SUCCESS: Archive recovered - ``{f.read()}''")
    except Exception as e:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        if (e.__class__.__name__ == "FileNotFoundError"):
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        elif (e.__class__.__name__ == "PermissionError"):
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        else:
            print(e)
    else:
        print("STATUS: Normal operations resumed")


def ft_main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("")

    ft_crisis_response("lost_archive.txt")
    print("")

    ft_crisis_response("classified_vault.txt")
    print("")

    ft_crisis_response("standard_archive.txt")
    print("")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    ft_main()
