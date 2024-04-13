from db.repositories.reservation_repository import ReservationRepository
from db.models.reservation_model import Reservation
from checkout.checkout import Checkout
from checkin.checkin import Checkin
class Menu:

    def print_main_menu(self):
        print("****************** Welcome to the LIRS system ******************\n")

        print("Please enter the number related to following option to continue:")

        print("________________________________________________________________\n")
        print("\t1: Check-out")
        print("\t2: Check-in")
        print("\t3: Exit")
        print("________________________________________________________________")

    def get_user_desired_option(self)-> int:
        user_option = 0
        
        #repeat while the input is not a number between 1 and 3
        while(int(user_option) not in range(1, 4)):
            user_option = input("Enter desired option: ")
            if(int(user_option) not in range(1, 4)):
                print("-->Please, enter a option beteween 1 and 3<--")
        #return the value option
        return int(user_option)


    def checkin(self):
        print("checkin selected")

    def handle_menu_option(option: int):
        if option == 1:
            Checkout().checkout()
        elif option == 2:
            Checkin().checkin()
        else:
            exit(1)

    def menu(self):
        #Run the menu in loop until the user ask to exit
        while True: 
            self.print_main_menu()

            user_option = self.get_user_desired_option()

            self.handle_menu_option(user_option)
