from flask_db_test.mongodb.connect_mongodb import connect_mongodb

conn = connect_mongodb()

blog_session_db = conn.blog_session_db
blog_ab = blog_session_db.blog_ab

blog_logs = blog_ab.find()
for log in blog_logs:
    print(log)
