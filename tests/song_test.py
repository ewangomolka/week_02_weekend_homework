import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song_1 = Song("Kiss from a rose")
        self.song_2 = Song("Gangstas' Paradise")
        self.song_3 = Song("Scrubs")

    def test_can_get_song_name(self):
        self.assertEqual("Kiss from a rose", self.song_1.name)

    