from datetime import datetime
from person import Actor, Guest
from play import GenreType, Play
from ticket import Ticket


def read_actors(filename: str) -> list[Actor]:
    actor_file = open(filename, "r")
    lines = actor_file.readlines()
    actors: list[Actor] = []
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        actor = Actor(
            split_line[0],
            datetime.strptime(split_line[1], '%Y.%m.%d')
        )
        actors.append(actor)
    
    actor_file.close()
    return actors

def read_guests(filename: str) -> list[Guest]:
    guest_file = open(filename, "r")
    lines = guest_file.readlines()
    guests: list[Guest] = []
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        guest = Guest(
            split_line[0],
            datetime.strptime(split_line[1], '%Y.%m.%d')
        )
        guests.append(guest)
    
    guest_file.close()
    return guests

def read_plays(filename: str) -> list[Play]:
    play_file = open(filename, "r")
    lines = play_file.readlines()
    plays: list[Play] = []
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        play = Play(
            split_line[1],
            split_line[0],
            GenreType(int(split_line[2])),
            int(split_line[3])
        )
        plays.append(play)
    
    play_file.close()
    return plays

def read_play2actor(filename, plays, actors) -> None:
    play2actor_file = open(filename, "r")
    lines = play2actor_file.readlines()
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        play_id = int(split_line[0])
        actor_id = int(split_line[1])
        plays[play_id].Actors.append(actors[actor_id])
        actors[actor_id].Plays.append(plays[play_id])
    play2actor_file.close()

def read_tickets(filename, guests, plays) -> list[Ticket]:
    ticket_file = open(filename, "r")
    lines = ticket_file.readlines()
    tickets: list[Ticket] = []
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        guest = guests[int(split_line[0])]
        play = plays[int(split_line[1])]
        ticket = Ticket(
            guest,
            play,
            price = int(split_line[2]),
            seat = split_line[3],
            DatOfPlay = datetime.strptime(split_line[4], '%Y.%m.%d')
        )
        tickets.append(ticket)
        guest.Tickets.append(ticket)
        play.Tickets.append(ticket)
    
    ticket_file.close()
    return tickets

def read_breaks(filename, plays) -> None:
    break_file = open(filename, "r")
    lines = break_file.readlines()
    for line in lines:
        split_line = [x.strip() for x in line.split(',')]
        play_id = int(split_line[0])
        plays[play_id].add_break(
            start = int(split_line[1]),
            end = int(split_line[2])
        )
    break_file.close()