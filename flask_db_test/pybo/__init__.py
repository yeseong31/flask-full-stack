import os

import pymongo
import pymysql
from flask import Flask

import config

MARIADB_CONN = pymysql.connect(
        host=os.getenv('MARIADB_HOST'),
        port=int(os.getenv('MARIADB_PORT')),
        user=os.getenv('MARIADB_USER'),
        passwd=os.getenv('MARIADB_PASSWORD'),
        db=os.getenv('MARIADB_DB_NAME'),
        charset='utf8')
MONGODB_CONN = pymongo.MongoClient(f'mongodb://{os.getenv("MONGODB_HOST")}')


def conn_mariadb():
    if not MARIADB_CONN:
        MARIADB_CONN.ping(reconnect=True)
    return MARIADB_CONN


def conn_mongodb(conn):
    try:
        conn.admin.command('ismaster')
    except:
        conn = pymongo.MongoClient(f'mongodb://{os.getenv("MONGODB_HOST")}')
    return conn.blog_session_db.blog_ab


mariadb = conn_mariadb()
cursor = mariadb.cursor()
mongo = conn_mongodb(MONGODB_CONN)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
