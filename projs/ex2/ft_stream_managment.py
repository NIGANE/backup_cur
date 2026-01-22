import sys


def ft_stream_managment() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("")
    arc_id = input("Input Stream active. Enter archivist ID: ")
    arc_report = input("Input Stream active. Enter status report: ")
    print("")
    sys.stdout.write(
        f"[STANDARD] Archive status from {arc_id}: All systems {arc_report}\n"
        )
    sys.stderr.write(
        "[ALERT] System diagnostic: Communication channels verified\n"
        )
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("")
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    ft_stream_managment()
