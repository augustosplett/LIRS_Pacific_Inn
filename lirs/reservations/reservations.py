from typing import List
from db.repositories.reservation_repository import ReservationRepository
from db.repositories.customer_repository import CustomerRepository
from db.repositories.rooms_repository import RoomsRepository
from db.models.reservation_model import Reservation
from db.models.customer_model import Customer

def handle_customer(first_name, last_name, email, phone_number)->Customer:
    customer_repository = CustomerRepository()

    my_customer = customer_repository.get_customer_by_email(email)
    
    if my_customer is None:
        # If customer don't exists create a new entry on db
        my_customer = Customer(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                phone_number=int(phone_number))
        
        customer_repository.create_customer(my_customer)
        my_customer = customer_repository.get_customer_by_email(my_customer.email)
    return my_customer

def handle_offline_reservations(filepath: str):
    
    data_array = load_offlineReservations(filepath)
    print("------------Loading offline reservations---------")
    for line in data_array:
        print("--------------------------------------------------")
        first_name = line[0]
        last_name = line[1]
        email = line[2]
        phone_number = line[3]
        room_type = line[4]
        days = int(line[5])

        #verify if the customer already exists
        my_customer = handle_customer(first_name, last_name, email, phone_number)

        #gets the room data
        my_room = RoomsRepository().get_room_by_room_type(room_type)
        #print(my_room)
        #if the room is available, make a reservation
        if my_room.avaliability >= 1:
            my_reserve = Reservation(my_room.id, my_customer.id, days, (my_room.room_price * days), 0)
            ReservationRepository().create_reservation(my_reserve)
            new_av_nu = my_room.avaliability - 1
            RoomsRepository().update_room_availability(my_room.id, new_av_nu)
            print(f"Reservation successfully Included for {my_customer.first_name} {my_customer.last_name} - {my_room.get_room_type()}")
        else:
            print(f"***No Room {my_room.room_type} available, impossible to finish reservation for {my_customer.first_name}.")

def load_offlineReservations(filepath: str) -> List[List[str]]:
    '''
    Load the offline reservations files and returns it's content in an array.
    '''
    # Open the file in read mode
    with open(filepath, 'r') as file:
        # Read the lines of the file
        lines = file.readlines()

    # Initialize an empty array
    data_array = []

    # Iterate over the lines
    for line in lines:
        # Split each line by comma and strip any whitespace
        cleaned_line = [item.strip() for item in line.strip().split(',')]
        # Add the element to the arrau
        data_array.append(cleaned_line)
    return data_array