def ft_vault_security(file_name: str, file_name2: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("")

    print("Initiating secure vault access...")
    try:
        with open(file_name, "r") as f:
            print("Vault connection established with failsafe protocols")
            print("")
            print("SECURE EXTRACTION:")
            print(f.read())
        print("")
        with open(file_name2, "r") as f_from:
            print("SECURE PRESERVATION:")
            text = f_from.read()
            print(text)
            with open(file_name, "a") as f_to:
                f_to.write("\n" + text)
            print("Vault automatically sealed upon completion")
        print("")
    except Exception as e:
        print(e)
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    ft_vault_security("classified_data.txt", "security_protocols.txt")
