from db.repositories.reservation_repository import ReservationRepository
from db.repositories.customer_repository import CustomerRepository
from db.repositories.rooms_repository import RoomsRepository
from db.models.reservation_model import Reservation
from db.models.customer_model import Customer
from db.models.rooms_model import Room

class Checkout:

    def __init__(self):
        self.open_reservations = ReservationRepository().get_open_reservations()

    def checkout(self):
        self.print_open_reserves()
        option = self.get_user_desired_reservation()
        self.print_checkout_details(option)

    def print_open_reserves(self):
        print("________________________________________________________________")
        print("Reservations available to checkout:")
        print("________________________________________________________________")
        for reserve in self.open_reservations:
            my_customer = reserve.get_reservation_properties()[1]
            info_to_print = f"Reserve #: {reserve.id} - Customer: {my_customer.first_name} {my_customer.last_name}"
            print(info_to_print)
        print("________________________________________________________________")

    def get_user_desired_reservation(self) -> Reservation:
        user_input = input("Enter the number of the reservation you want to close: ")
        while not self.get_open_reservation_by_id(user_input) != None:
            print("Invalid reservation number. Please try again.")
            user_input = input("Enter the number of the reservation you want to close: ")
        return self.get_open_reservation_by_id(user_input)
    
    def get_open_reservation_by_id(self, user_input) -> Reservation:
        for reservation in self.open_reservations:
            if user_input == str(reservation.id):
                return reservation
        return None

    def print_checkout_details(self, reservation: Reservation):
        print("________________________________________________________________")
        print("________________________Pacific Inn_____________________________")
        print("Your invoice information is:")
        print(f"\tName: {reservation.get_reservation_properties()[1].first_name} {reservation.get_reservation_properties()[1].last_name}")
        print(f"\tAccomodation: {reservation.accommodation_days} days")
        print(f"\tRoom Type: {reservation.get_reservation_properties()[0].get_room_type()}")
        print(f"\tTotal Cost: {reservation.cost} $")
        print("_______________Thank you and see you next time._________________")