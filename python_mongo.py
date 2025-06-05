import pymongo
import os
import dotenv

dotenv.load_dotenv()


def insert_data_log(data_logs) :
    
    DB_USER = os.environ.get("DB_USER")
    DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DB_HOST = os.environ.get("DB_HOST")
    DB_DATABASE = os.environ.get("DB_DATABASE")
    DB_COLLECTION = os.environ.get("DB_COLLECTION")
    
    # Client pour le serveur mongodb
    client_mongodb = pymongo.MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:27017')
    data = client_mongodb.get_database(DB_DATABASE).get_collection(DB_COLLECTION)
    #insertion des données
    data.insert_one(data_logs)
 





