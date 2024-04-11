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

    def get_customers(self) -> list[Customer]:
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM inn_customer"
            cursor.execute(sql)
            records = cursor.fetchall()
            return records

    def get_customer_by_id(self, id:int)-> Customer:
            sql = "SELECT * FROM inn_customer where id = %s"
            with self.connection.cursor() as cursor:
                cursor.execute(sql, id)
            record = cursor.fetchone()
            if record:
                return Customer(id=record[0], first_name=record[1], last_name=record[2], email=record[3], phone_number=record[4])
            else:
                return None

    def update_customer(self, id: int, customer: Customer):
        cursor = connection.cursor()
        sql = "UPDATE tabela_exemplo SET nome = %s, idade = %s WHERE id = %s"
        values = (nome, idade, id)
        cursor.execute(sql, values)
        connection.commit()
        print("Registro atualizado com sucesso!")

    # Exemplo de uso:
    # connection = mysql.connector.connect(...)  # Conectar ao banco de dados
    # update_record(connection, 1, "Maria Silva", 35)

    def delete_customer(self, id: int):
        cursor = connection.cursor()
        sql = "DELETE FROM tabela_exemplo WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        connection.commit()
        print("Registro excluído com sucesso!")

    # Exemplo de uso:
    # connection = mysql.connector.connect(...)  # Conectar ao banco de dados
    # delete_record(connection, 1)
