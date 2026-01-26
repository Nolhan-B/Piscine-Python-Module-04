def handle_archive_access(filename: str) -> None:
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception as error:
        print(f"RESPONSE: Unexpected system anomaly - {error}")
        print("STATUS: Crisis handled, system stabilized")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")

    archives = [
        "lost_archive.txt",
        "classified_vault.txt",
        "standard_archive.txt"
    ]

    for archive in archives:
        if archive == "standard_archive.txt":
            print(f"ROUTINE ACCESS: Attempting access to '{archive}'...")
        else:
            print(f"CRISIS ALERT: Attempting access to '{archive}'...")

        handle_archive_access(archive)
        print()

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
