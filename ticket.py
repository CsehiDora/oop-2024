from person import Guest
from datetime import datetime

class Ticket:
    @property
    def Owner(self) -> Guest:
        return self._Owner
    
    @Owner.setter
    def Owner(self, value: Guest) -> None:
        self._Owner = value

    @property
    def Price(self) -> int:
        return self._Price
    
    @Price.setter
    def Price(self, value: int) -> None:
        self._Price = value

    @property
    def Seat(self) -> int:
        return self._Seat
    
    @Seat.setter
    def Seat(self, value: int) -> None:
        self._Seat = value

    @property
    def Play(self):
        return self._Play
    
    @Play.setter
    def Play(self, value: Play) -> None:
        self._Play = value

    @property
    def DateOfPlay(self) -> datetime:
        return self._DateOfPlay
    
    @DateOfPlay.setter
    def DateOfPlay(self, value: datetime) -> None:
        self._DateOfPlay = value

    def __str__(self) -> str:
        return f"{self._Play.Title}, {self._DateOfPlay}"

    def __init__(self, owner, play, price = 0, seat = 0, DatOfPlay = datetime.today()) -> None:
        self._Owner = owner
        self._Play = play
        self._Price = price
        self._Seat = seat
        self._DateOfPlay = DatOfPlay