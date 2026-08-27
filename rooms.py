"""
rooms.py
--------
Contains the Room class, which represents a room in the hotel.
"""


class Room:
    """Represents a hotel room (number, type, price per night, and availability status)."""

    def __init__(self, room_number, room_type, price_per_night):
        self._room_number = room_number
        self._room_type = room_type
        self._price_per_night = price_per_night
        self._is_available = True   # every room is available by default when created

    # ---------- Getters ----------
    def get_room_number(self):
        return self._room_number

    def get_room_type(self):
        return self._room_type

    def get_price_per_night(self):
        return self._price_per_night

    def is_available(self):
        return self._is_available
        
    # ---------- Setters (Update feature) ----------
    def set_price_per_night(self, new_price):
        self._price_per_night = new_price
 
    def set_room_type(self, new_type):
        self._room_type = new_type
 

    # ---------- Behaviour ----------
    def mark_as_booked(self):
        self._is_available = False

    def mark_as_available(self):
        self._is_available = True

    def display_info(self):
        status = "Available" if self._is_available else "Booked"
        return (f"Room {self._room_number} | Type: {self._room_type} | "
                f"Price/Night: {self._price_per_night} | Status: {status}")

    def __str__(self):
        return self.display_info()
