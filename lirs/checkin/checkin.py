import re
from db.repositories.rooms_repository import RoomsRepository
from db.repositories.customer_repository import CustomerRepository
from db.models.rooms_model import Room
from db.models.customer_model import Customer

class Checkin:

    def checkin(self):
        print("________________________________________________________________")
        print("PACIFIC INN: WELCOME TO CHECKIN")
        print("Chose one of the options bellow:")
        print("________________________________________________________________")
        selected_room = self.handle_room_selection()
        if selected_room is not None:
            customer = self.handle_customer_information()

    def validate_email(self, email):
        '''
        Validate if the input email is valid
        '''
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    def handle_customer_information(self)-> Customer:
        #asks for email to try to find if the user already exists:
        customer_email = input("Please, enter customer's email:")
        while not self.validate_email(customer_email):
            print("Please, enter a valid email e.g.: 'name@copr.com'")
            customer_email = input("Please, enter customer's email:")
        #validate if the user already exists:
        c_repository = CustomerRepository()
        customer = c_repository.get_customer_by_email(customer_email)
        #create the customer if it doens't exist
        if customer is None:
            print("Customer not found, please, fill the customer information to create one:")
            #handle the customer creation
            first_name = input("First Name:")
            last_name = input("Last Name:")
            phone = int(input("Phone Number:"))
            c_repository.create_customer(Customer(first_name=first_name, 
                                                  last_name=last_name,
                                                  email=customer_email,
                                                  phone_number=phone))
            customer = c_repository.get_customer_by_email(customer_email)
        #return customer
        return customer

    def handle_room_selection(self) -> Room:
        ''' 
        Function responsible for printitng the room information in the screen and capture the user selection
        '''
        rooms = RoomsRepository().get_rooms()
        for room in rooms:
            print(room)

        print("________________________________________________________________")
        user_input = int(input("Enter the desired room's ID: ").strip())
        while self.room_is_in_the_list(rooms, user_input) == None:
            print("Invalid ID, please, inform a valid one.")
            user_input = int(input("Enter the desired room's ID: ").strip())

        selected_room = self.room_is_in_the_list(rooms, user_input)
        if not selected_room.avaliability > 0:
            print(f"*** Sorry no {selected_room.get_room_type()} available ***")
        else:
            return selected_room
        return None

    def room_is_in_the_list(self, room_list: list[Room], id: int)->Room:
        '''
        Function to find a room in a list using the ID
        '''
        for room in room_list:
            if room.id == id:
                return room
        return None