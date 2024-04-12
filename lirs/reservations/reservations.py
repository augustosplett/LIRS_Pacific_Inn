from typing import List
from db.repositories.reservation_repository import ReservationRepository
from db.models.reservation_model import Reservation

def handle_offline_reservations(filepath: str):
    data_array = load_offlineReservations(filepath)

    # Print the array
    print(data_array)

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