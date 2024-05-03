from datetime import datetime
from abc import ABC
from abc import abstractmethod

class Person(ABC):
    @abstractmethod
    def Name(self) -> str:
        pass

    @abstractmethod
    def DayOfBirth(self) -> datetime:
        pass
    
    @abstractmethod
    def Age(self):
        pass
    
    def __init__(self, name: str, dayofbirth: datetime) -> None:
        self._Name = name
        self._DayOfBirth = dayofbirth
    
    def __str__(self) -> str:
        return f"{self._Name}, {self._DayOfBirth.strftime("%Y.%m.%d")}"

class Actor(Person):
    @property
    def Plays(self) -> list:
        return self._Plays
    
    @property
    def DayOfBirth(self) -> datetime:
        return self._DayOfBirth
    
    @DayOfBirth.setter
    def DayOfBirth(self, value: datetime) -> None:
        self._DayOfBirth = value

    def Age(self) -> int:
        diff = datetime.today() - self._DayOfBirth
        return int(diff.days)//365
    
    @property
    def Name(self) -> str:
        return self._Name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._Name = value
    
    def __init__(self, name = "", dayofbirth = datetime.today()) -> None:
        super().__init__(name, dayofbirth)
        self._Plays = []

class Guest(Person):
    @property
    def Tickets(self) -> list:
        return self._Tickets
    
    @property
    def DayOfBirth(self) -> datetime:
        return self._DayOfBirth
    
    @DayOfBirth.setter
    def DayOfBirth(self, value: datetime) -> None:
        self._DayOfBirth = value

    def Age(self) -> int:
        diff = datetime.today() - self._DayOfBirth
        return int(diff.days)//365

    @property
    def Name(self) -> str:
        return self._Name
    
    @Name.setter
    def Name(self, value: str) -> None:
        self._Name = value

    def __init__(self, name = "", dayofbirth = datetime.today()) -> None:
        super().__init__(name, dayofbirth)
        self._Tickets = []