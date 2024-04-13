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
        finally:
            cursor.close()

    def get_rooms(self) -> list[Room]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_rooms"
                cursor.execute(sql)
                records = cursor.fetchall()
                return records
        except mysql.connector.Error as e:
            print(f"Something went wrong to get the Rooms: {e}")
        finally:
            cursor.close()

    def get_room_by_room_type(self, room_type: str) -> Room:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_rooms WHERE room_type = %s"
                cursor.execute(sql, (room_type,))
                record = cursor.fetchone()
                return Room(id=record[0], room_type=record[1], room_price=record[2], avaliability=record[3])
        except mysql.connector.Error as e:
            print(f"Something went wrong to get the Rooms: {e}")
        finally:
            cursor.close()

    def get_room_by_room_id(self, id: int) -> Room:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_rooms WHERE id = %s"
                cursor.execute(sql, (id,))
                record = cursor.fetchone()
                return Room(id=record[0], room_type=record[1], room_price=record[2], avaliability=record[3])
        except mysql.connector.Error as e:
            print(f"Something went wrong to get the Rooms: {e}")
        finally:
            cursor.close()


    def update_room_availability(self, id: int, available_rooms: int):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE inn_rooms SET avaliability = %s WHERE id = %s"
                values = ( available_rooms, id)
                cursor.execute(sql, values)
                self.connection.commit()
            #print(f"Number of Available Rooms successfully Updated")
        except mysql.connector.Error as e:
            print(f"Something went wrong to update the room availability: {e}")
        finally:
            cursor.close()    
