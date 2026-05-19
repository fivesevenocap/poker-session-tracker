from models import PokerSession
from database import connect_db, create_tables, save_session


def main() -> None:
    connect_db()
    create_tables()

    session = PokerSession(
        date="2026-05-18",
        duration=2.5,
        hands_played=450,
        buy_in=2.0,
        profit=7.35,
        room="PokerOK",
        limit="NL2",
        notes="Good focus, no tilt",
    )
    save_session(session)
    
    print(session.summary())


if __name__ == "__main__":
    main()
