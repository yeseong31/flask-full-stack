from flask_db_test.pymysql.connect_mariadb import connect_mariadb

# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

# 삽입할 데이터
email = 'test@test.com'
blog_id = 'A'

sql = f'INSERT INTO user_info (email, blog_id) values ("{email}", "{blog_id}")'
cursor.execute(sql)
db_conn.commit()
