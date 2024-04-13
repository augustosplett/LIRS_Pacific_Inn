from db.repositories.customer_repository import CustomerRepository
from db.repositories.rooms_repository import RoomsRepository
from db.models.customer_model import Customer
from db.models.rooms_model import Room
from typing import Tuple

class Reservation:

    def __init__(self, room_id: int, customer_id: int, accommodation_days: int, cost:float, checkout:int, id: int = None):
        self.room_id = room_id
        self.customer_id = customer_id
        self.accommodation_days = accommodation_days
        self.cost = cost
        self.checkout = checkout
        self.id = id  

    def get_reservation_properties(self)-> Tuple[Room, Customer]:
        try:
            my_customer = CustomerRepository().get_customer_by_id(self.customer_id)
            my_romm = RoomsRepository().get_room_by_room_id(self.room_id)
            return (my_romm, my_customer)
        except Exception as e:
            print(f"Something went wrong to retrive the reservation details: {e}")