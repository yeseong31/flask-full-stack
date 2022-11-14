from flask_login import UserMixin
from config import conn_mariadb


class User(UserMixin):
    def __init__(self, user_id, email, blog_id):
        self.id = user_id
        self.email = email
        self.blog_id = blog_id
    
    def get_id(self):
        return str(self.id)
    
    @staticmethod
    def get(user_id: str):
        """user_id를 통해 사용자 정보 조회"""
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"SELECT * FROM user_info WHERE user_id='{user_id}'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        
        if not user:
            db_cursor.close()
            return None
        
        user = User(user_id=user[0], email=user[1], blog_id=user[2])
        db_cursor.close()
        return user
    
    @staticmethod
    def find(email: str):
        """email을 통해 사용자 정보 조회"""
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"SELECT * FROM user_info WHERE email='{email}'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        
        if user is not None:
            user = User(user_id=user[0], email=user[1], blog_id=user[2])
        db_cursor.close()
        return user
    
    @staticmethod
    def create(email: str, blog_id: str):
        """email, blog_id 정보를 통해 사용자 생성"""
        user = User.find(email)
        
        if user is not None:
            return user
        
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"INSERT INTO user_info (email, blog_id) VALUES ('{email}', '{blog_id}')"
        db_cursor.execute(sql)
        maria_db.commit()
        return User.find(email)
    
    @staticmethod
    def delete(user_id: str):
        """user_id를 가지는 사용자 삭제"""
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"DELETE FROM user_info WHERE user_id='{user_id}'"
        deleted = db_cursor.execute(sql)
        maria_db.commit()
        
        return deleted
