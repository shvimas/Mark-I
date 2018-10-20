import configparser
import os

import pymongo

with open(os.path.join(os.path.dirname(__file__), '../../envs/mongo-env.list')) as f:
    dummy_section = '[default]'
    cfg = dummy_section + '\n' + f.read()
    cfg_parser = configparser.ConfigParser()
    cfg_parser.read_string(cfg)
    __mongo_user = cfg_parser[dummy_section]['MONGO_INITDB_ROOT_USERNAME']
    __mongo_pass = cfg_parser[dummy_section]['MONGO_INITDB_ROOT_PASSWORD']

try:
    # noinspection PyStatementEffect
    __mongo_user
    # noinspection PyStatementEffect
    __mongo_pass
except NameError:
    raise EnvironmentError('Failed to get credentials for MongoDB')


def get_mongo_client(host: str = 'localhost', port: int = 27018) -> pymongo.MongoClient:
    return pymongo.MongoClient(f'mongodb://{__mongo_user}:{__mongo_pass}@{host}:{port}')
