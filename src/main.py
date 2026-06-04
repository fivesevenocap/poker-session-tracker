import sys
from models import PokerSession
from database import create_tables, get_sessions, save_session


def show_sessions() -> None:
    sessions = get_sessions()

    if not sessions:
        print("No sessions found.")
        return
    print(
    f"{'#':<3}"
    f"{'Date':<13}"
    f"{'Room':<10}"
    f"{'Limit':<7}"
    f"{'Hours':<7}"
    f"{'Hands':<7}"
    f"{'Buy-in':<8}"
    f"{'Profit':<7}"
)
    print("-" * 62)
    for index, session in enumerate(sessions, start=1):
        print(
            f"{index:<3}"
            f"{session.date:<13}"
            f"{session.room:<10}"
            f"{session.limit:<7}"
            f"{session.duration:<7}"
            f"{session.hands_played:<7}"
            f"{session.buy_in:<8.2f}"
            f"{session.profit:<7.2f}"
        )

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
    if total_sessions > 0:
        average_profit = total_profit / total_sessions
    else:
        average_profit = 0
    if total_hours > 0:
        profit_per_hour = total_profit / total_hours
    else:
        profit_per_hour = 0
    print("Your stats:")
    print(f"Total sessions: {total_sessions}")
    print(f"Total profit: {total_profit}")
    print(f"Total hands: {total_hands}")
    print(f"Total hours: {total_hours}")
    print(f"Average profit per session: {average_profit:.2f}$")
    print(f"Profit per hour: {profit_per_hour:.2f}$/h")

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

