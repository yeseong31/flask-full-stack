from flask_login import UserMixin
from config import conn_mariadb


class User(UserMixin):
    def __init__(self, user_id, user_email, blog_id):
        self.id = user_id
        self.user_email = user_email
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
        
        user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user
    
    @staticmethod
    def find(user_email: str):
        """user_email을 통해 사용자 정보 조회"""
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"SELECT * FROM user_info WHERE user_email='{user_email}'"
        db_cursor.execute(sql)
        user = db_cursor.fetchone()
        
        if user is not None:
            user = User(user_id=user[0], user_email=user[1], blog_id=user[2])
        db_cursor.close()
        return user
    
    @staticmethod
    def create(user_email: str, blog_id: str):
        """user_email, blog_id 정보를 통해 사용자 생성"""
        user = User.find(user_email)
        
        if user is not None:
            return user
        
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"INSERT INTO user_info (user_email, blog_id) VALUES ('{user_email}', '{blog_id}')"
        db_cursor.execute(sql)
        maria_db.commit()
        return User.find(user_email)
    
    @staticmethod
    def delete(user_id: str):
        """user_id를 가지는 사용자 삭제"""
        maria_db = conn_mariadb()
        db_cursor = maria_db.cursor()
        
        sql = f"DELETE FROM user_info WHERE user_id='{user_id}'"
        deleted = db_cursor.execute(sql)
        maria_db.commit()
        
        return deleted
