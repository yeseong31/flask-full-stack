from db_test.mongodb.connect_mongodb import connect_mongodb

conn = connect_mongodb()

blog_session_db = conn.blog_session_db
blog_ab = blog_session_db.blog_ab

result = blog_ab.find_one({'emailid': 'jhleeroot@gmail.com'})
print(result)
