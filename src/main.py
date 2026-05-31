import sys
from models import PokerSession
from database import create_tables, get_sessions, save_session


def show_sessions() -> None:
    sessions = get_sessions()

    if not sessions:
        print("No sessions found.")
        return

    for session in sessions:
        print(session.summary())

def add_session() -> None:
    date = input("[1/8] Session date (YYYY-MM-DD): ")
    room = input("[2/8] Poker room: ")
    limit = input("[3/8] Limit: ")
    duration = float(input("[4/8] Duration (hours): "))
    hands = int(input("[5/8] Hands played: "))
    buyin = float(input("[6/8] Buy-in: "))
    profit = float(input("[7/8] Profit: "))
    notes = input("[8/8] Notes:")
    session = PokerSession(
    date=date,
    duration=duration,
    hands_played=hands,
    buy_in=buyin,
    profit=profit,
    room=room,
    limit=limit,
    notes=notes,
)
    save_session(session)
    print("Session saved successfully.")

def show_stats() -> None:
    sessions = get_sessions()
    total_sessions = len(sessions)
    total_profit = 0.0
    total_hands = 0
    total_hours = 0.0
    for session in sessions:
        total_profit = total_profit + session.profit
        total_hands = total_hands + session.hands_played
        total_hours = total_hours + session.duration
    print("Your stats:")
    print(f"Total sessions: {total_sessions}")
    print(f"Total profit: {total_profit}")
    print(f"Total hands: {total_hands}")
    print(f"Total hours: {total_hours}")

def main() -> None:
    create_tables()

    command = sys.argv[1] if len(sys.argv) > 1 else "show"

    if command == "show":
        show_sessions()
    elif command == "add":
        add_session()
    elif command == "stats":
        show_stats()
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()

