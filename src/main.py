import sys

from database import create_tables, get_sessions


def show_sessions() -> None:
    sessions = get_sessions()

    if not sessions:
        print("No sessions found.")
        return

    for session in sessions:
        print(session.summary())


def main() -> None:
    create_tables()

    command = sys.argv[1] if len(sys.argv) > 1 else "show"

    if command == "show":
        show_sessions()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
