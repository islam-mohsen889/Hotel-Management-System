"""
main.py
-------
Demonstration / test-drive of the Hotel Management System.
No input() is used — all objects and operations are predefined, as required.
"""

from hotel import HotelSystem
from models import Guest, Employee
from rooms import Room
from reservations import Reservation, Payment


def main():
    system = HotelSystem()

    # ============================================================
    # 1. Create / Register objects
    # ============================================================
    print("========== ADDING EMPLOYEES ==========")
    emp1 = Employee(1, "Sara Ahmed", "sara@hotel.com", "Receptionist")
    emp2 = Employee(2, "Omar Khaled", "omar@hotel.com", "Manager")
    system.addEmployee(emp1)
    system.addEmployee(emp2)

    print("\n========== ADDING GUESTS ==========")
    guest1 = Guest(101, "Ali Hassan", "ali@example.com")
    guest2 = Guest(102, "Mona Yousef", "mona@example.com")
    guest3 = Guest(103, "Karim Adel", "karim@example.com")
    system.addGuest(guest1)
    system.addGuest(guest2)
    system.addGuest(guest3)

    print("\n========== ADDING ROOMS ==========")
    room1 = Room(201, "Single", 500)
    room2 = Room(202, "Double", 800)
    room3 = Room(203, "Suite", 1500)
    system.addRoom(room1)
    system.addRoom(room2)
    system.addRoom(room3)

    # ============================================================
    # 2. Display
    # ============================================================
    print("\n========== AVAILABLE ROOMS (before booking) ==========")
    system.displayAvailableRooms()

    # ============================================================
    # 3. Relationship Operation: create reservations
    # ============================================================
    print("\n========== CREATING RESERVATIONS ==========")
    res1 = Reservation(1, guest1, room1, "2026-09-01", "2026-09-05")
    system.createReservation(res1)

    res2 = Reservation(2, guest2, room2, "2026-09-03", "2026-09-06")
    system.createReservation(res2)

    # ============================================================
    # 4. Calculation
    # ============================================================
    print("\n========== RESERVATION COSTS ==========")
    print(f"Total cost for {guest1.get_name()}: {res1.calculate_total_price()} EGP")
    print(f"Total cost for {guest2.get_name()}: {res2.calculate_total_price()} EGP")

    # ============================================================
    # 5. Payment
    # ============================================================
    print("\n========== RECORDING PAYMENT ==========")
    payment1 = Payment(1, res1, res1.calculate_total_price(), "Credit Card")
    system.addPayment(payment1)
    payment1.display_payment()

    # ============================================================
    # 6. Display all reservations
    # ============================================================
    system.displayReservations()

    # ============================================================
    # 7. Update feature
    # ============================================================
    print("\n========== UPDATING DATA ==========")
    system.updateRoomPrice(203, 1800)
    print(room3)
    system.updateGuestContact(102, "mona.new@example.com")

    # ============================================================
    # 8. Remove / Delete: cancel a reservation
    # ============================================================
    print("\n========== CANCELLING A RESERVATION ==========")
    system.cancelReservation(res2)

    print("\n========== AVAILABLE ROOMS (after cancellation) ==========")
    system.displayAvailableRooms()

    # ============================================================
    # 9. Search
    # ============================================================
    print("\n========== SEARCHING ==========")
    system.searchGuest("Ali Hassan")
    system.searchGuest("Not A Real Guest")
    system.searchRoom(202)

    # ============================================================
    # 10. Validation / edge cases
    # ============================================================
    print("\n========== VALIDATION: booking an unavailable room ==========")
    # room1 is still booked by Ali Hassan (res1 was never cancelled)
    res3 = Reservation(3, guest3, room1, "2026-09-10", "2026-09-12")
    system.createReservation(res3)

    print("\n========== VALIDATION: cancelling a reservation that isn't active ==========")
    # res3 was rejected above, so it was never actually added to the system
    system.cancelReservation(res3)

    print("\n========== VALIDATION: updating a room that doesn't exist ==========")
    system.updateRoomPrice(999, 100)

    print("\n========== VALIDATION: updating a guest that doesn't exist ==========")
    system.updateGuestContact(999, "ghost@example.com")


if __name__ == "__main__":
    main()
