import os
import requests
import dotenv
import logging
import json
from time import gmtime, strftime
from python_mongo import insert_data_log

dotenv.load_dotenv()
horodatage_log = strftime("%Y-%m-%d", gmtime())
horodatage_report = strftime("%Y-%m-%d", gmtime())

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
    if API_TOKEN and API_URL and APPS:
        params = { "app" : APPS}
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(API_URL, params, headers=headers)
        data = response.json()
   
        if  data :
            data_obj = json.loads(response.text)
            insert_data_log(data_obj)
            
            with open(f'reports/data_report_{horodatage_report}.json', 'a+') as file :
                if file :
                    file.write(json.dump(data, file, indent=4))
                    file.write('\n')
    else :
        raise ValueError(f'Erreur : le token et/ou le URL et/ou le nom de l\'application sont manquantes')
except Exception as e :
    print(e)
    logging.error(e.args[0])





