from db.models.customer_model import Customer
from db.db_utils import connect_to_mysql
import mysql.connector
import os

class CustomerRepository:

    def __init__(self):
        #get the current path
        path = os.getcwd()
        #build the full db config path
        full_configuration_path = path + '/lirs/config/database.ini'
        #print(full_configuration_path)
        self.connection = connect_to_mysql(full_configuration_path)

    def create_customer(self, customer: Customer):
        try:
            sql = "INSERT INTO inn_customer (first_name, last_name, email, phone_number) VALUES (%s, %s, %s, %s)"
            values = (customer.first_name, customer.last_name, 
                      customer.email, customer.phone_number)

            with self.connection.cursor() as cursor:
                cursor.execute(sql, values)
            self.connection.commit()
            print(f"New customer: {customer.first_name} {customer.last_name} successfully inserted")
        except mysql.connector.Error as e:
            print(f"Error to insert the customer: {e}")
        finally:
            cursor.close()

    def get_customers(self) -> list[Customer]:
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM inn_customer"
                cursor.execute(sql)
                records = cursor.fetchall()
                return records
        except mysql.connector.Error as e:
            print(f"Error to get the customers: {e}")
        finally:
            cursor.close()

    def get_customer_by_email(self, email: str) -> Customer:
        try:
            sql = "SELECT * FROM inn_customer WHERE email = %s"
            
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (email,)) 
                record = cursor.fetchone()
                if record is not None:
                    return Customer(id=record[0], first_name=record[1], last_name=record[2], email=record[3], phone_number=record[4])
                else:
                    return None
        except mysql.connector.Error as e:
            print(f"Error to get the customer: {e}")
        finally:
            cursor.close()

    def get_customer_by_id(self, id:int)-> Customer:
        try:
            sql = "SELECT * FROM inn_customer where id = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, id)
            record = cursor.fetchone()
            if record:
                return Customer(id=record[0], first_name=record[1], last_name=record[2], email=record[3], phone_number=record[4])
            else:
                return None
        except mysql.connector.Error as e:
            print(f"Error to get the customer: {e}")
        finally:
            cursor.close()

    def update_customer(self, id: int, customer: Customer):
        try:
            with self.connection.cursor() as cursor:
                sql = "UPDATE inn_customer SET first_name = %s, last_name = %s, email = %s, phone_number = %s WHERE id = %s"
                values = (customer.first_name, customer.last_name, 
                        customer.email, customer.phone_number, id)
                cursor.execute(sql, values)
                self.connection.commit()
            print("Customer successfully updated")
        except mysql.connector.Error as e:
            print(f"Error to update the customer: {e}")
        finally:
            cursor.close()

    def delete_customer(self, id: int):
        try:
            with self.connection.cursor() as cursor:
                sql = "DELETE FROM inn_customer WHERE id = %s"
                cursor.execute(sql, (id,))
                self.connection.commit()
            print("Customer successfully deleted!")
        except mysql.connector.Error as e:
            print(f"Error to delete the customer: {e}")
        finally:
            cursor.close()