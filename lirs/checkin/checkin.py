from db.repositories.rooms_repository import RoomsRepository
from db.models.rooms_model import Room

class Checkin:

    def checkin(self):
        print("________________________________________________________________")
        print("PACIFIC INN: WELCOME TO CHECKIN")
        print("Chose one of the options bellow:")
        print("________________________________________________________________")
        selected_room = self.handle_room_selection()
        if selected_room is not None:
            self.handle_customer_information()

    def handle_customer_information():
        pass
    
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