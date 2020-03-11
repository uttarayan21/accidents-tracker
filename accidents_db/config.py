import os
import json

with open(os.getcwd() + '/config.json', 'r') as config:
    config = json.load(config)

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = config.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    DB = config.get('DB')
    SQLALCHEMY_DATABASE_URI = f"{DB.get('DB_TYPE')}://{DB.get('DB_USER')}:{DB.get('DB_PASSWORD')}@{DB.get('DB_HOST')}/{DB.get('DB_NAME')}"
