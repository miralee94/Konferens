from filemanager import FileManager


class Room():
    def __init__(self, room_id, name, time, status):
        self.room_id = room_id
        self.name = name
        self.time = time
        self.status = status

    def __str__(self) -> str:
        return f"Room ID: {self.room_id} Name: {self.name} Tid: {self.time} Status: {self.status}"

class Booking:
    def __init__(self):
        self.booking = list()
        imported_rooms = FileManager.read_rooms()
        for room in imported_rooms:
            room_id, name, time, status = room.split(",")
            self.booking.append(Room(room_id, name, time, status))

    def print_all_rooms(self):
        for room in self.booking:
            print(room)

    def print_booked_rooms(self):
        for room in self.booking:
            if room.status == "bokad":
                print(room)

    def add_to_booking(self):
        self.print_all_rooms()
        room_id = int(input("ID: "))
        room_time = input("Ange tid för bokning: ")
        self.booking[room_id].status = "Bokad"
        self.booking[room_id].time = room_time

    def remove_from_booking(self):
        self.print_all_rooms()
        room_id = int(input("ID: "))
        self.booking[room_id].status = "Ledig"

    def finalize_booking(self):
        print("Saving your booking to file")
        FileManager.save_room_booking(self.booking)
        self.__init__()

