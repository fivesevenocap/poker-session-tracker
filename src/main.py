from models import PokerSession


def main() -> None:
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

    print(session.summary())


if __name__ == "__main__":
    main()
