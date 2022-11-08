from flask_db_test.pymysql.connect_mariadb import connect_mariadb

# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

# user_info 테이블 삭제
sql = 'DROP TABLE user_info;'
cursor.execute(sql)
db_conn.commit()

sql = 'SHOW TABLES;'
print(cursor.execute(sql))    # 0: 테이블이 비어 있음을 의미
