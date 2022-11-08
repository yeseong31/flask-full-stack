from db_test.pymysql.connect_mariadb import connect_mariadb

# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

# user_id가 1인 데이터 삭제
user_id = 1
sql = f'DELETE FROM user_info WHERE user_id={user_id}'
print(cursor.execute(sql))
db_conn.commit()
