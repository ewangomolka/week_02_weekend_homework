
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