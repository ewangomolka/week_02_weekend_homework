
import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest
from src.karaoke_bar import KaraokeBar

class TestKaraokeBar(unittest.TestCase):
    def setUp(self):
        self.karaoke_bar = KaraokeBar("Sultans of Sing!", 500.00)
        self.room_1 = Room("Room 1", 2, 10.00)
        self.room_2 = Room("Room 2", 3, 15.00)
        self.room_3 = Room("Room 3", 5, 20.00)
        self.guest_1 = Guest("Dean Pelton", 30.00, "Kiss from a rose")
        self.guest_2 = Guest("Jeff Winger", 20.00, "Ganstas Paradise")
        self.guest_3 = Guest("Britta Perry", 15.00, "No Scrubs")
        self.guest_4 = Guest("Ben Chang", 17.50, "The Final Countdown")
        # self.guests = {
        #     "name": "Dean Pelton",
        #     "wallet": 30.00,
        #     "fav song": "Kiss from a rose"
        # },
        # {
        #     "name": "Jeff Winger",
        #     "wallet": 20.00,
        #     "fav song": "Gangstas Paradise"
        # },
        # {
        #     "name": "Britta Perry",
        #     "wallet": 15.00,
        #     "fav song": "No Scrubs"
        # },
        # {
        #     "name": "Ben Chang",
        #     "wallet": 17.50,
        #     "fav song": "The Final Countdown"
        # }
        self.song_1 = Song("Kiss from a rose")
        self.song_2 = Song("Blitzkrieg Bop")
        self.song_3 = Song("Careless Whisper")
        self.song_4 = Song("Pokemon Theme")
        self.song_5 = Song("Umbrella")

    def test_can_get_name_of_karaoke_bar(self):
        self.assertEqual("Sultans of Sing!", self.karaoke_bar.name)

    def test_can_add_money_to_till(self):
        self.karaoke_bar.increase_till(10.00)
        self.assertEqual(510.00, self.karaoke_bar.till)

    def test_can_get_change_from_till(self):
        self.karaoke_bar.decrease_till(10)
        self.assertEqual(490.00, self.karaoke_bar.till)

    def test_guest_can_pay_for_room(self):
        self.guest_1.pay_entry(self.room_1)
        self.karaoke_bar.increase_till(self.room_1.price)
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(510.00, self.karaoke_bar.till)
        self.assertEqual(1, len(self.room_1.guests))
    
    def test_guest_cannot_pay_for_room(self):
        guest_funds = self.guest_3.pay_entry(self.room_3)
        self.assertEqual("can't afford", guest_funds)

    

    def test_if_room_has_favourite_song(self):
        self.room_1.add_song(self.song_1)
        self.room_1.add_song(self.song_4)
        self.guest_1.pay_entry(self.room_1)
        self.guest_2.pay_entry(self.room_1)
        self.karaoke_bar.increase_till(self.room_1.price)
        self.karaoke_bar.increase_till(self.room_1.price)
        self.room_1.check_in_guest(self.guest_1)
        self.room_1.check_in_guest(self.guest_2)
        self.guest_1.room_has_guests_favourite_song(self.room_1.songs)
        print(self.room_1.songs)
        self.assertEqual(2, len(self.room_1.songs))
        self.assertEqual(520.00, self.karaoke_bar.till)
        self.assertEqual("Whoo!", self.guest_1.room_has_guests_favourite_song(self.room_1.songs))

