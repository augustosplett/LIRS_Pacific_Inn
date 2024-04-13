import os
from db.db_utils import check_db_exist
from reservations.reservations import handle_offline_reservations
from menu import menu
from db.models.customer_model import Customer
from db.repositories.customer_repository import CustomerRepository

#######################################################
#Check the DB
#######################################################
#get the current path
path = os.getcwd()
#build the full db config path
full_configuration_path = path + '/lirs/config/database.ini'
#check if the DB exists and create if if no.
check_db_exist(full_configuration_path)

#######################################################
#Process reservations made offline (.txt file)
#######################################################
full_offline_reservation_path = path + '/lirs/reservations/reservation_file.txt'
handle_offline_reservations(full_offline_reservation_path)


#connect to the db considering the information on the configuration file 
#conexao = connect_to_mysql(full_configuration_path)

#call the main menu
#menu()

# test = CustomerRepository()
# customer = Customer( "Priscilla", "Luz", "augusto@gmail.com", 4381112222)
# print(customer)
#test.update_customer(2, customer)
#test.delete_customer(2)