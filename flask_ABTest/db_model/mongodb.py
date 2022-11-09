import os

import pymongo
from dotenv import load_dotenv

load_dotenv(verbose=True)

MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_CONN = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')


def conn_mongodb():
    try:
        MONGODB_CONN.admin.command('ismaster')
        blog_ab = MONGODB_CONN.blog_session_db.blog_ab
    except:
        conn = pymongo.MongoClient(f'mongodb://{MONGODB_HOST}')
        blog_ab = conn.blog_session_db.blog_ab
    return blog_ab
