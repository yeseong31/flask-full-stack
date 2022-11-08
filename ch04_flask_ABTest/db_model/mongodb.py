import os

import pymongo
from dotenv import load_dotenv

load_dotenv(verbose=True)

MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_CONN = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')


def conn_mongodb(conn):
    try:
        conn.admin.command('ismaster')
    except:
        conn = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')
    finally:
        blog_ab = conn.blog_session_db.blog_ab
    return blog_ab


if __name__ == '__main__':
    conn_mongodb(MONGODB_CONN)
