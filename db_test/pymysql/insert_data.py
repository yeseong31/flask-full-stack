from db_test.pymysql.connect_mariadb import connect_mariadb

# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

# 삽입할 데이터
user_email = 'test@test.com'
blog_id = 'A'

sql = f'INSERT INTO user_info (user_email, blog_id) values ("{user_email}", "{blog_id}")'
cursor.execute(sql)
db_conn.commit()
