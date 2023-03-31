
import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("Room 1", 2, 10.00)
        self.room_2 = Room("Room 2", 3, 15.00)
        self.room_3 = Room("Room 3", 5, 20.00)
        self.guest_1 = Guest("Dean Pelton", 30.00, "Kiss from a rose")
        self.guest_2 = Guest("Jeff Winger", 20.00, "Ganstas Paradise")
        self.guest_3 = Guest("Britta Perry", 15.00, "No Scrubs")
        self.guest_4 = Guest("Ben Chang", 17.50, "The Final Countdown")
        self.song_1 = Song("Kiss from a rose")
        self.song_2 = Song("Blitzkrieg Bop")
        self.song_3 = Song("Careless Whisper")
        self.song_4 = Song("Pokemon Theme")
        self.song_5 = Song("Umbrella")

    def test_add_guest_to_room(self):
        self.room_1.check_in_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_remove_guest_from_room(self):
        self.room_1.check_in_guest(self.guest_4)
        self.room_1.check_out_guest(self.guest_4)
        self.assertEqual(0, len(self.room_1.guests))

    def test_check_in_multiple_guests(self):
        self.room_2.check_in_guest(self.guest_1)
        self.room_2.check_in_guest(self.guest_2)
        self.room_2.check_in_guest(self.guest_4)
        self.assertEqual(3, len(self.room_2.guests))

    def test_add_song_to_room(self):
        self.room_1.add_song(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_add_multiple_songs_to_room(self):
        self.room_2.add_song(self.song_2)
        self.room_2.add_song(self.song_4)
        self.room_2.add_song(self.song_3)
        self.assertEqual(3, len(self.room_2.songs))

    def test_can_get_names_of_songs_in_room(self):
        self.room_2.add_song(self.song_2)
        self.room_2.add_song(self.song_4)
        self.room_2.add_song(self.song_3)
        self.assertEqual([self.song_2, self.song_4, self.song_3], self.room_2.songs)


    
