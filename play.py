from datetime import datetime
from person import Actor, Guest
from ticket import Ticket
from enum import Enum

class GenreType(Enum):
    Drama = 1
    Opera = 2
    Comedy = 3
    Tragedy = 4

    def __str__(self) -> str:
        return self.name

class Play:
    @property
    def Title(self) -> str:
        return self._Title
    
    @Title.setter
    def Title(self, value: str) -> None:
        self._Title = value

    @property
    def Author(self) -> str:
        return self._Author
    
    @Author.setter
    def Author(self, value: str) -> None:
        self._Author = value

    def __init__(self) -> None:
        pass

    @property
    def Length(self) -> int:
        return self._Length
    
    @Length.setter
    def Length(self, value: int) -> None:
        self._Length = value

    @property
    def Genre(self) -> GenreType:
        return self._Genre
    
    @Genre.setter
    def Genre(self, value: GenreType) -> None:
        self._Genre = value

    # ListOfTickets
    @property
    def Tickets(self) -> list:
        return self._Tickets
    
    def buy_ticket(self, buyer: Guest, price: int, seat: str, date: datetime) -> None:
        ticket = Ticket(buyer, self, price, seat, date)
        self._Tickets.append(ticket)
        buyer.Tickets.append(ticket)

    # ListOfBreaks
    @property
    def Breaks(self) -> list:
        return self._Breaks
    
    def add_break(self, start: int, end: int) -> None:
        _break = Break(start, end, self)
        self._Breaks.append(_break)

    # ListOfActor
    @property
    def Actors(self) -> list:
        return self._Actors
    
    def add_actor(self, actor: Actor) -> None:
        self._Actors.append(actor)
        actor.Plays.append(self)

    def __init__(self, author = "", title = "", genre = GenreType.Tragedy, length = 0) -> None:
        self._Author = author
        self._Title = title
        self._Genre = genre
        self._Length = length
        self._Breaks = []
        self._Actors = []
        self._Tickets = []

    def __str__(self) -> str:
        return f"{self._Title}, {self._Author}, {self._Genre}, {self._Length}"

class Break:
    @property
    def Play(self) -> Play:
        return self._Play
    
    @Play.setter
    def Play(self, value: Play) -> None:
        self._Play = value

    @property
    def Start(self) -> int:
        return self._Start
    
    @Start.setter
    def Start(self, value: int) -> None:
        self._Start = value

    @property
    def End(self) -> int:
        return self._End
    
    @End.setter
    def End(self, value: int) -> None:
        self._End = value

    def __init__(self, start: int, end: int, play: Play = None) -> None:
        self._Start = start
        self._End = end
        self._Play = play