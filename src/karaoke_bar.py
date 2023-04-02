
class KaraokeBar:
    def __init__(self, name, till):
        self.name = name
        self.till = till

    def increase_till(self, amount):
        self.till += amount

    def decrease_till(self, amount):
        self.till -= amount

    # def room_has_guests_favourite_song(self, song, room):
    #     for song in room:
    #         if song == room.songs:
    #             return "Whoo!"
    #         else:
    #             return None

