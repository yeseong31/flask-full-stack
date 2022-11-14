import os.path

import pymongo
import pymysql
from dotenv import load_dotenv

# https://velog.io/@yvvyoon/python-env-dotenv
load_dotenv(verbose=True)

BASE_DIR = os.path.dirname(__file__)

# MongoDB 접속 설정
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_CONN = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')

# MariaDB 접속 설정
MARIADB_CONN = pymysql.connect(
    host=os.getenv('MARIADB_HOST'),
    port=int(os.getenv('MARIADB_PORT')),
    user=os.getenv('MARIADB_USER'),
    passwd=os.getenv('MARIADB_PASSWORD'),
    db=os.getenv('MARIADB_DB_NAME'),
    charset='utf8')

SECRET_KEY = os.getenv('SECRET_KEY')


def conn_mongodb():
    """MongoDB 연결 확인"""
    try:
        MONGODB_CONN.admin.command('ismaster')
        blog_ab = MONGODB_CONN.blog_session_db.blog_ab
    except:
        conn = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')
        blog_ab = conn.blog_session_db.blog_ab
    return blog_ab


def conn_mariadb():
    """MariaDB 연결 확인"""
    if not MARIADB_CONN.open:
        MARIADB_CONN.ping(reconnect=True)
    return MARIADB_CONN
