import os

import pymysql
from dotenv import load_dotenv

load_dotenv(verbose=True)


def connect_mariadb():
    return pymysql.connect(
        host=os.getenv('MARIADB_HOST'),
        port=int(os.getenv('MARIADB_PORT')),
        user=os.getenv('MARIADB_USER'),
        passwd=os.getenv('MARIADB_PASSWORD'),
        db=os.getenv('MARIADB_DB_NAME'),
        charset='utf8')


# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

# 연결 해제
db_conn.close()
