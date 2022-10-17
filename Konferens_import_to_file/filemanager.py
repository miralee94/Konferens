class FileManager:
    def read_rooms():
        with open("rooms.txt", "r", encoding='utf-8') as file:
            return file.read().splitlines()

    def save_room_booking(rooms):
        with open('rooms.txt', 'w', encoding='utf-8') as file:
            for room in rooms:
                file.write(f"{room.room_id},{room.name},{room.time},{room.status}\n")
