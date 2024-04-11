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
            print("Customer successfully inserted")
        except mysql.connector.Error as e:
            print(f"Erro to insert the customer: {e}")


    def get_customer_by_id(self, id:int):
        # Implementação para ler um registro
        pass

    def update_customer(self, id: int, customer: Customer):
        # Implementação para atualizar um registro
        pass

    def delete_customer(self, id: int):
        # Implementação para excluir um registro
        pass
