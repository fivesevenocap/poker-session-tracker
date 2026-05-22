import sqlite3
from models import PokerSession
def connect_db():
    connection = sqlite3.connect("data/poker_tracker.db")
    return connection
def create_tables() -> None:
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            duration REAL NOT NULL,
            hands_played INTEGER NOT NULL,
            buy_in REAL NOT NULL,
            profit REAL NOT NULL,
            room TEXT NOT NULL,
            limit_name TEXT NOT NULL,
            notes TEXT
        )
    """)

    connection.commit()
    connection.close()
def save_session(session: PokerSession) -> None:
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO sessions (
            date,
            duration,
            hands_played,
            buy_in,
            profit,
            room,
            limit_name,
            notes
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            session.date,
            session.duration,
            session.hands_played,
            session.buy_in,
            session.profit,
            session.room,
            session.limit,
            session.notes,
        ),
    )

    connection.commit()
    connection.close()
    
def get_sessions() -> list[PokerSession]:
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT date, duration, hands_played, buy_in, profit, room, limit_name, notes FROM sessions")

    rows = cursor.fetchall()

    sessions = []

    for row in rows:
        session = PokerSession(
            date=row[0],
            duration=row[1],
            hands_played=row[2],
            buy_in=row[3],
            profit=row[4],
            room=row[5],
            limit=row[6],
            notes=row[7],
        )
        sessions.append(session)

    connection.close()

    return sessions