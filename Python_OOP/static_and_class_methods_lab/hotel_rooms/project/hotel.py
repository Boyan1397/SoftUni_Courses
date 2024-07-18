from typing import List
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms: List[Room] = []
    
    @property
    def guests(self):
        return sum([room.guests for room in self.rooms if room.is_taken])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        return room.take_room(people)

    def free_room(self, room_number):
        room = next(filter(lambda r: r.number == room_number, self.rooms))
        return room.free_room()

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join(free_rooms)}\n"
                f"Taken rooms: {', '.join(taken_rooms)}\n"
                )