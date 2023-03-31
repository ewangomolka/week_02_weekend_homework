
import unittest
from src.guest import Guest
from src.room import Room

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Dean Pelton", 30.00, "Kiss from a rose")
        self.guest_2 = Guest("Jeff Winger", 20.00, "Gangstas Paradise")
        self.guest_3 = Guest("Britta Perry", 5.00, "No Scrubs")
        self.room_1 = Room("Room 1", 2, 10.00)

    def test_can_get_total_cash_from_guest_1(self):
        expected_value = 30.00
        actual_value = self.guest_1.wallet
        self.assertEqual(expected_value, actual_value)

    def test_guest_has_favourite_song(self):
        expected_value = "Gangstas Paradise"
        actual_value = self.guest_2.fav_song
        self.assertEqual(expected_value, actual_value)

    def test_guest_has_name(self):
        expected_value = "Britta Perry"
        actual_value = self.guest_3.name
        self.assertEqual(expected_value, actual_value)

    def test_guest_can_pay_for_karaoke(self):
        guest_funds = self.guest_1.pay_entry(self.room_1)
        self.assertEqual("can afford", guest_funds)

    def test_guest_cannot_pay_for_entry(self):
        guest_funds = self.guest_3.pay_entry(self.room_1)
        self.assertEqual("can't afford", guest_funds)

