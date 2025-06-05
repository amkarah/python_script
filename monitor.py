import os
import requests
import dotenv
import logging
import json
from time import gmtime, strftime
from python_mongo import insert_data_log
from db import create_tables, deploy_release
from utils import create_directory

dotenv.load_dotenv()
horodatage_log = strftime("%Y-%m-%d", gmtime())
horodatage_report = strftime("%Y-%m-%d", gmtime())

create_directory()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s Data: %(args)s',
    handlers=[ 
        # logging.StreamHandler(), 
        logging.FileHandler(f'logs/log_monitor_{horodatage_log}.log'),
    ],
)


API_TOKEN = os.environ.get("API_TOKEN")
API_URL= os.environ.get("URL_API")
APPS = os.environ.get("APPS")



try:
    #creation de la table
    create_tables()

    
    if API_TOKEN and API_URL and APPS:
        params = { "app" : APPS}
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(API_URL, params, headers=headers)
        data = response.json()
   
        if  data :
            data_obj = json.loads(response.text)
            #insertion Mysql
            timestamp = strftime("%Y-%m-%d %H:%m:%S", gmtime(data_obj['timestamp']))
            deploy_release(data_obj['app'], data_obj['status'], data_obj['response_time'], timestamp)
  
            with open(f'reports/data_report_{horodatage_report}.json', 'a+') as file :
                if file :
                    file.write(json.dump(data, file, indent=4))
                    file.write('\n')
    else :
        raise ValueError(f'Erreur : le token et/ou le URL et/ou le nom de l\'application sont manquantes')
except Exception as e : 
    #insertion Mongo
    insert_data_log({
        "message": str(e.args[0])
    })
    logging.error(e.args[0])





