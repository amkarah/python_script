import mysql.connector
import dotenv
import os

dotenv.load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD_MYSQL"),
    "database": os.getenv("DB_DATABASE_MYSQL"),
}

def connection_to_database():
    return mysql.connector.connect(**DB_CONFIG)


def create_tables(): 
    with connection_to_database() as connection:
        with connection.cursor() as cursor:
      
            cursor.execute("""
                 CREATE TABLE IF NOT EXISTS app_status (
                id int auto_increment primary key,
                timestamp datetime,
                app_name varchar(255),
                status varchar(50),
                response_time float
                )""")
            
    
def deploy_release(app_name, status, response_time, timestamp) :
    with connection_to_database()  as connection :
        with connection.cursor() as cursor:
            cursor.execute(""" INSERT INTO app_status (app_name, status, response_time, timestamp) VALUES (%s, %s, %s, %s)""", (app_name, status, response_time, timestamp ))
            connection.commit()