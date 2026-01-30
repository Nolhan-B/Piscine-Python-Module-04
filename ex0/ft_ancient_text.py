def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    file_name = "ancient_fragment.txt"

    print(f"Accessing Storage Vault: {file_name}")
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print("Connection established...")
    print("RECOVERED DATA:")
    content = file.read()
    print(content)

    file.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
