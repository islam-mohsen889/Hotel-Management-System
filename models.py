class Person:

    def __init__(self, person_id, name, contact_info):
        self.person_id = person_id
        self.name = name
        self.contact_info = contact_info

    def get_id(self):
        return self.person_id

    def get_name(self):
        return self.name

    def get_contact(self):
        return self.contact_info
        
    def set_contact(self, new_contact_info):
        self.contact_info = new_contact_info

    def display_info(self):
        print("ID:", self.person_id)
        print("Name:", self.name)
        print("Contact:", self.contact_info)



class Guest(Person):

    def __init__(self, person_id, name, contact_info):
        super().__init__(person_id, name, contact_info)
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def remove_reservation(self, reservation):
        if reservation in self.reservations:
            self.reservations.remove(reservation)
            print("Reservation removed successfully.")
        else:
            print("Reservation not found.")

    def display_reservations(self):
        if not self.reservations:
            print("No reservations found.")
        else:
            print(f"Reservations for {self.name}:")
            for reservation in self.reservations:
                print(reservation)


class Employee(Person):

    def __init__(self, person_id, name, contact_info, position):
        super().__init__(person_id, name, contact_info)
        self.position = position

    def get_position(self):
        return self.position

    def display_info(self):
        super().display_info()
        print("Position:", self.position)
