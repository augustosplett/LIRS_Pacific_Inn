from db.models.rooms_model import Room
from db.db_utils import connect_to_mysql
import mysql.connector
import os

class RoomsRepository:

    def __init__(self):
        #get the current path
        path = os.getcwd()
        #build the full db config path
        full_configuration_path = path + '/lirs/config/database.ini'

        self.connection = connect_to_mysql(full_configuration_path)
    
    def insert_room(self, room:Room):
        try:
            with self.connection.cursor() as cursor:
                insert_query = """
                    INSERT INTO rooms (room_type, room_price, avaliability) 
                    VALUES (%(room_type)s, %(room_price)s, %(avaliability)s)
                """
                room_data = {
                    'room_type': room.room_type,
                    'room_price': room.room_price,
                    'avaliability': room.avaliability
                }
                cursor.execute(insert_query, room_data)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Something went wrong to insert the Rooms: {e}")

    def get_rooms(self) -> list[Room]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_rooms"
                cursor.execute(sql)
                records = cursor.fetchall()
                return records
        except mysql.connector.Error as e:
            print(f"Something went wrong to get the Rooms: {e}")

    def update_room_availability(self, id: int, available_rooms: int):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE inn_rooms SET avaliability = %s WHERE id = %s"
                values = (id, available_rooms)
                cursor.execute(sql, values)
                self.connection.commit()
            print("Number of Available Rooms successfully Updated")
        except mysql.connector.Error as e:
            print(f"Something went wrong to update the room availability: {e}")