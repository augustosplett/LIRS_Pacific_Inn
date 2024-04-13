import os
from db.db_utils import check_db_exist
from reservations.reservations import handle_offline_reservations
from menu.menu import Menu

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

#######################################################
#Calls the system menu
#######################################################
Menu().menu()