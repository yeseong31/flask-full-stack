import os

import pymysql

from dotenv import load_dotenv

load_dotenv(verbose=True)

MARIADB_CONN = pymysql.connect(
    host=os.getenv('MARIADB_HOST'),
    port=int(os.getenv('MARIADB_PORT')),
    user=os.getenv('MARIADB_USER'),
    passwd=os.getenv('MARIADB_PASSWORD'),
    db=os.getenv('MARIADB_DB_NAME'),
    charset='utf8')


def conn_mariadb():
    if not MARIADB_CONN:
        MARIADB_CONN.ping(reconnect=True)
    return MARIADB_CONN
