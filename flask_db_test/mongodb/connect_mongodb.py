import os

import pymongo
from dotenv import load_dotenv

load_dotenv(verbose=True)


def connect_mongodb():
    username = os.getenv('MONGODB_USERNAME')
    password = os.getenv('MONGODB_PASSWORD')
    ip_address = os.getenv('MONGODB_IP_ADDRESS')
    connection = pymongo.MongoClient('mongodb://%s' % ip_address)
    # connection = pymongo.MongoClient()
    # connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
    return connection


conn = connect_mongodb()

# 연결 확인
# print(conn.admin.command('ismaster'))
# print()
# print(conn.server_info())
