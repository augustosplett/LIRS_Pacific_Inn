import configparser
import mysql.connector

def read_db_configuration(configuration_file: str)-> tuple:
    '''
    Read the configurations on the configuration file
    '''
    #print(configuration_file)
    config = configparser.ConfigParser()
    config.read(configuration_file)

    db_config = {}
    if 'mysql' in config:
        db_config['host'] = config['mysql']['host']
        db_config['database'] = config['mysql']['database']
        db_config['user'] = config['mysql']['user']
        db_config['password'] = config['mysql']['password']

    return db_config

def connect_to_mysql(configuration_file: str):
    '''
    return the connection to the database
    '''
    config = read_db_configuration(configuration_file)
    #print(config)
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            #print("Conectado ao banco de dados MySQL")
            return connection
    except mysql.connector.Error as e:
        print(f"Error to connect MySQL: {e}")
    return None

def db_exists(cursor, db_name: str)->bool:
    '''
        Rerturn if the desired database exists or not
    '''
    try:
        cursor.execute("SHOW DATABASES")
        dbs = [db[0] for db in cursor.fetchall()]
        
        if db_name not in dbs:
            return False
        else:
            return True
    except mysql.connector.Error as e:
        print(f"Error to validade if the database exists: {e}")


def create_db(cursor, db_name):
    '''
    Create the tables using the given cursor on the given db
    '''
    try:
        #if database doesn't exist, create it
        cursor.execute("CREATE DATABASE {}".format(db_name))
        #use the created database
        cursor.execute("USE {}".format(db_name))
        #Create the tables
        scripts_sql = [
            """
            CREATE TABLE `inn_customer` (
                `id` int NOT NULL AUTO_INCREMENT,
                `first_name` varchar(50) DEFAULT NULL,
                `last_name` varchar(50) DEFAULT NULL,
                `email` varchar(50) DEFAULT NULL,
                `phone_number` bigint DEFAULT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
            """,
            """
            CREATE TABLE `inn_rooms` (
                `id` int NOT NULL AUTO_INCREMENT,
                `room_type` varchar(1) DEFAULT NULL,
                `room_price` decimal(5,2) DEFAULT NULL,
                `avaliability` smallint DEFAULT NULL,
                PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
            """,
            """
            CREATE TABLE `inn_reservation` (
                `id` int NOT NULL AUTO_INCREMENT,
                `room_id` int DEFAULT NULL,
                `customer_id` int DEFAULT NULL,
                `accomodation_days` smallint DEFAULT NULL,
                `cost` decimal(5,2) DEFAULT NULL,
                `checkout` tinyint DEFAULT NULL,
                PRIMARY KEY (`id`),
                KEY `room_id` (`room_id`),
                KEY `customer_id` (`customer_id`),
                CONSTRAINT `inn_reservation_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `inn_rooms` (`id`),
                CONSTRAINT `inn_reservation_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `inn_customer` (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
            """ 
        ]
        # execute the scripts to create the tables
        for script in scripts_sql:
            cursor.execute(script)
    except mysql.connector.Error as e:
        print(f"Error to create tables: {e}")

def check_db_exist(configuration_file):
    '''
    Function responsible for validate if the database exists
    '''
    #read db configurations
    config = read_db_configuration(configuration_file)
    try:
        #stablish the connection
        conn = mysql.connector.connect(
                host=config['host'],
                user=config['user'],
                password=config['password']
            )

        # Cursor para executar comandos SQL
        with conn.cursor() as cursor:
            exist = db_exists(cursor,config['database'] )

            if not exist:
                create_db(cursor,config['database'])
            
        conn.close()
    except mysql.connector.Error as e:
        print(f"Error to validade if the database exists: {e}")