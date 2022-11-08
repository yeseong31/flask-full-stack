from db_test.pymysql.connect_mariadb import connect_mariadb

# DB 연결
db_conn = connect_mariadb()
cursor = db_conn.cursor()

sql = 'SELECT * FROM user_info'
cursor.execute(sql)

for result in cursor.fetchall():
    print(result, type(result))
    
# user_id가 1인 사용자 데이터 조회
user_id = 1
sql = f'SELECT * FROM user_info WHERE user_id={user_id}'
print(cursor.execute(sql))
