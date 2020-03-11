import os
import json
from accidents_db.config import Config as db_config
with open(os.getcwd()+'/config.json') as config:
    config = json.load(config)

class Config(db_config):
    SECRET_KEY = config.get('SECRET_KEY')
