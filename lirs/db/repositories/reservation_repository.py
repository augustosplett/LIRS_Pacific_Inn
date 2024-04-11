from db.models.reservation_model import Reservation
from db.db_utils import connect_to_mysql
import mysql.connector
import os

class ReservationRepository:
        
    def __init__(self):
        #get the current path
        path = os.getcwd()
        #build the full db config path
        full_configuration_path = path + '/lirs/config/database.ini'
        #print(full_configuration_path)
        self.connection = connect_to_mysql(full_configuration_path)

    def get_open_reservations(self) -> list[Reservation]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_reservation where checkout = 0"
                cursor.execute(sql)
                records = cursor.fetchall()
                return records
        except mysql.connector.Error as e:
            print(f"Something went wrong to get the open Reservations: {e}")

    def get_reservation_by_id(self, id:int)-> Reservation:
        try:
            sql = "SELECT * FROM inn_reservation where id = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, id)
            record = cursor.fetchone()
            if record:
                return Reservation(room_id = record[0], customer_id = record[1], accommodation_days = record[2], cost = record[3], checkout = record[4], id = record[5])
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error to get the reservation: {e}")

    def update_reservation_status(self, id: int, status: int):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE inn_reservation SET checkout = %s WHERE id = %s"
                values = (status, id)
                cursor.execute(sql, values)
                self.connection.commit()
            print("Reservation Status successfully Updated")
        except mysql.connector.Error as e:
            print(f"Something went wrong to update the reservation status: {e}")