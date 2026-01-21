def main() -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    vault_filename = "classified_vault.txt"

    print("Initiating secure vault access...")

    try:
        with open(vault_filename, "r") as file:
            print("Vault connection established with failsafe protocols")
            print("\nSECURE EXTRACTION:")
            for line in file:
                print(f"[CLASSIFIED] {line}")
    except FileNotFoundError:
        print(f"ERROR: Vault '{vault_filename}' not found for extraction")
    except Exception as e:
        print(f"ERROR: Unexpected issue during extraction: {e}")

    try:
        with open(vault_filename, "w") as file:
            print("\nSECURE PRESERVATION:")
            file.write("[CLASSIFIED] New security protocols archived\n")
            print("[CLASSIFIED] New security protocols archived")
    except Exception as e:
        print(f"ERROR: Unexpected issue during preservation: {e}")
    print("Vault automatically sealed upon completion")

    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
