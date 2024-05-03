from itertools import groupby
from readDataFunctions import read_actors, read_breaks, read_guests, read_play2actor, read_plays, read_tickets
from ticket import Ticket
from person import Actor, Guest, Person
from play import Play, GenreType
from datetime import datetime

def get_oldest_person(person: Person) -> Person:
    return max(person, key=lambda p: p.Age())

def plays_in_april(tickets: list[Ticket]) -> list[Play]:
    april_tickets = list(
        filter(
            lambda t:
                t.DateOfPlay.year == 2024
                and t.DateOfPlay.month == 4,
            tickets
        )
    )

    # halmazt készítünk az előadásokból => minden előadás egyszer szerepeljen
    playSet = set()
    for ticket in april_tickets:
        playSet.add(ticket.Play)

    return list(playSet)

def most_viewed_plays(plays: list[Play]) -> list[Play]:
    # lekérdezzük, hogy hányszor nézték meg a legnézetteb színdarabot
    max_views = len(max(plays, key=lambda p: len(p.Tickets)).Tickets)
    # leszürjük a legnézetteb színdarabokat
    return list(filter(lambda p: len(p.Tickets) == max_views, plays))

def most_viewed_play_per_guest(tickets: list[Ticket]) -> list[(Guest, Play)]:
    result: list[(Guest, Play)] = []
    # a kulcs szerint rendezett listát tudja jól csoportosítani!!
    # https://medium.com/codex/python-groupby-tricks-234004132c14
    # nézők sezrint csoportosítjuk a jegyeket
    for guest, ticket_values in groupby(sorted(tickets, key=lambda t: t.Owner.Name), key=lambda t: t.Owner):
        # listát csinálunk a néző jegyeihez tartozó színdarabokból
        guest_plays: list[Play] = [t.Play for t in list(ticket_values)]
        # a fenti listából kiszedjük a leggyakoribb színdarabot
        most_viewed_play: Play = max(guest_plays, key=lambda p: guest_plays.count(p))
        # az néző-színdarab értékpárt hozzáadjuk a végeredményhez
        result.append((guest, most_viewed_play))
    return result

def romeo_and_juliet_in_october(tickets: list[Ticket]) -> int:
    # csak az októberi R&J jegyek
    filtered_tickets = list(
        filter(
            lambda t:
                t.DateOfPlay.year == 2024
                and t.DateOfPlay.month == 10
                and t.Play.Title == "Romeo es Julia",
            tickets
        )
    )

    # halmazt készítünk a dátumokból
    dates = set()
    for ticket in filtered_tickets:
        dates.add(ticket.DateOfPlay)

    # minden dátum egy-egy előadás
    return len(dates)

def main():
    Actors = read_actors('beadandó/Actors.csv')
    Guests = read_guests('beadandó/Guests.csv')
    Plays = read_plays('beadandó/Plays.csv')
    Tickets = read_tickets('beadandó/Ticket.csv', Guests, Plays)
    read_breaks('beadandó/Break.csv', Plays)
    read_play2actor('beadandó/Play2actor.csv', Plays, Actors)

    print("Ki a legidosebb szinesz?")
    oldest_actor = get_oldest_person(Actors)
    print(oldest_actor.Name)

    print("\nMelyik szindarabot adtak 2024 aprilisaban?")
    for play_title in plays_in_april(Tickets):
        print(play_title.Title)

    print("\nMelyik szindarabhoz adtak el a legtobb jegyet?")
    for play_title in most_viewed_plays(Plays):
        print(play_title.Title)

    print("\nMelyik nezo melyik szindarabot latta a legtobbszor?")
    for guest, play in most_viewed_play_per_guest(Tickets):
        print(f"{guest.Name}: {play.Title}")

    print("\nMennyiszer fogjak adni 2024 oktobereben a Romeo es Juliat?")
    print(romeo_and_juliet_in_october(Tickets))

if __name__ == "__main__":
    main()