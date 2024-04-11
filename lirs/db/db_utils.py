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
        print(f"Erro ao conectar ao banco de dados MySQL: {e}")
    return None