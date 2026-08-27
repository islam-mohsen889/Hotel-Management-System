from datetime import datetime
class Reservation:
    """reservation for a room at a hotel."""
    def __init__(self, reservation_id, guest, room, check_in_date, check_out_date):
        self.reservation_id = reservation_id
        self.guest = guest
        self.room = room
        self.check_in_date = self.convert_date(check_in_date)
        self.check_out_date = self.convert_date(check_out_date)
        if self.check_out_date <= self.check_in_date:
            raise ValueError("Check-out date must be after check-in date")
        self.status = "confirmed"

    def convert_date(self, date_str):
      if isinstance(date_str, datetime):
            return date_str
      return datetime.strptime(date_str, "%Y-%m-%d")

    def get_reservation_id(self):
      return self.reservation_id
    def get_guest(self):
      return self.guest
    def get_room(self):
      return self.room
    def get_check_in_date(self):
      return self.check_in_date
    def get_check_out_date(self):
      return self.check_out_date
    def get_status(self):
      return self.status

    def calculate_total_price(self):
        nights = (self.check_out_date - self.check_in_date).days
        return nights * self.room.get_price_per_night()

    def cancel(self):
        self.status = "Cancelled"
        self.room.mark_as_available()

    def display_info(self):
       print("Reservation ID:", self.reservation_id)
       print("Guest:", self.guest.get_name())
       print("Room:", self.room.get_room_number())
       print("Room Type:", self.room.get_room_type())
       print("Check-in:", self.check_in.strftime("%Y-%m-%d"))
       print("Check-out:", self.check_out.strftime("%Y-%m-%d"))
       print("Status:", self.status)
       print("Total Cost:", self.calculate_total_price())


class Payment:
  def __init__(self, payment_id, reservation, amount, payment_method):
        self._payment_id = payment_id
        self.reservation = reservation
        self.amount = amount
        self.payment_method = payment_method

  def get_payment_id(self):
    return self._payment_id
  def get_reservation(self):
    return self.reservation
  def get_amount(self):
    return self.amount
  def get_payment_method(self):
    return self.payment_method

  def display_payment(self):
    print("Payment ID:", self._payment_id)
    print("Reservation:", self.reservation.get_reservation_id())
    print("Amount:", self.amount)
    print("Payment Method:", self.payment_method)