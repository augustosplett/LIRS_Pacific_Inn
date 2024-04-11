from menu import menu
from db.db_utils import *
import os

from db.models.customer_model import Customer
from db.repositories.customer_repository import CustomerRepository

# #get the current path
# path = os.getcwd()
# #build the full db config path
# full_configuration_path = path + '/lirs/config/database.ini'

# #connect to the db considering the information on the configuration file 
# conexao = connect_to_mysql(full_configuration_path)

#call the main menu
#menu()

test = CustomerRepository()
customer = Customer( "Priscilla", "Luz", "augusto@gmail.com", 4381112222)
print(customer)
#test.update_customer(2, customer)
#test.delete_customer(2)