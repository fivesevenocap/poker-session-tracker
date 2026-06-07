from dataclasses import dataclass


@dataclass
class PokerSession:
    id: int
    date: str
    duration: float
    hands_played: int
    buy_in: float
    profit: float
    room: str
    limit: str
    notes: str 

    def summary(self) -> str:
        return (
            f"{self.date} | {self.room} | {self.limit} | "
            f"{self.duration}h | {self.hands_played} hands | "
            f"profit: {self.profit}$"
        )