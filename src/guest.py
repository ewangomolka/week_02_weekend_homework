
class Guest:
    def __init__(self, name, wallet, fav_song):
        self.name = name
        self.wallet = wallet
        self.fav_song = fav_song

    def pay_entry(self, room):
        if self.wallet >= room.price:
            self.wallet -= room.price
            return "can afford"
        elif self.wallet < room.price:
            return "can't afford"
        
    def room_has_guests_favourite_song(self, songs):
        for song in songs:
            if self.fav_song == song.name:
                return "Whoo!"
            else:
                return None
        # found_song = [song for song in room.songs if song[0] == "Kiss from a rose"]
        # return "Whoo!"