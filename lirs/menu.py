def print_main_menu():
    print("****************** Welcome to the LIRS system ******************\n")

    print("Please enter the number related to following option to continue:")

    print("________________________________________________________________\n")
    print("\t1: Check-out")
    print("\t2: Check-in")
    print("\t3: Exit")
    print("________________________________________________________________")

def get_user_desired_option()-> int:
    user_option = 0
    
    #repeat while the input is not a number between 1 and 3
    while(int(user_option) not in range(1, 4)):
        user_option = input("Enter desired option: ")
        if(int(user_option) not in range(1, 4)):
            print("Please, enter a option beteween 1 and 3")
    
    #return the value option
    return int(user_option)

def checkout():
    print("checkout selected")

def checkin():
    print("checkin selected")

def handle_menu_option(option: int):
    if option == 1:
        checkout()
    elif option == 2:
        checkin()
    else:
        exit(1)

def menu():
    #Run the menu in loop until the user ask to exit
    while True: 
        print_main_menu()

        user_option = get_user_desired_option()

        handle_menu_option(user_option)