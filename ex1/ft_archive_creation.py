def main() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")

    file_archive = open(filename, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")

    file_archive.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")

    file_archive.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")

    file_archive.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 003] Archived by Data Archivist trainee")

    file_archive.close()
    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
