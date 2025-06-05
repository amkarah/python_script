import os
import requests
import dotenv
import logging

dotenv.load_dotenv()





logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s Data: %(args)s',
    handlers=[ 
        # logging.StreamHandler(), 
        logging.FileHandler('logs/log_monitor.log'),
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
        json = response.json()
        if  json :
            with open('reports/file.txt', 'a+') as file :
                for key, value in json.items() :
                    file.write( f'{key} :  {value} \n')
                file.write('\n')
        
    else :
        raise ValueError(f'Erreur : le token et/ou le URL et/ou le nom de l\'application sont manquantes')
except Exception as e :
    logging.error(e.args[0])





