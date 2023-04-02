
class Room:
    def __init__(self, name, guest_capacity, price):
        self.name = name
        self.guest_capacity = guest_capacity
        self.price = price
        self.guests = []
        self.songs = []

    
    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def add_song(self, song):
        self.songs.append(song)

    def check_room_capacity(self):
        if len(self.guests) > self.guest_capacity:
            return "Room over capacity"
        else:
            return "Room available"

    # def room_has_guests_favourite_song(self, guest, song):
    #     for song in self.songs:
    #         if song == guest.fav_song:
    #             return "Whoo!"
    #         else:
    #             return None

    