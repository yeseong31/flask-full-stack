from flask_db_test.pymysql.connect_mariadb import connect_mariadb

db_conn = connect_mariadb()
cursor = db_conn.cursor()

# user_info 테이블 생성
sql = """
CREATE TABLE user_info (
    user_id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_email VARCHAR(100) NOT NULL,
    blog_id CHAR(4),
    PRIMARY KEY (user_id)
);
"""
cursor.execute(sql)
db_conn.commit()

sql = 'SHOW TABLES;'
print(cursor.execute(sql))    # 1: 테이블이 생성되었음을 의미
