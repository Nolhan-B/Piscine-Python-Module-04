import sys


def main() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    id = input("Input Stream active. Enter archivist ID: ")
    rep = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {id}: {rep}\n", file=sys.stdout)

    print("[ALERT] System diagnostic: "
          "Communication channels verified\n", file=sys.stderr)

    print("[STANDARD] Data transmission complete\n", file=sys.stdout)

    print("\nThree-channel communication test successful.", file=sys.stdout)


if __name__ == "__main__":
    main()
