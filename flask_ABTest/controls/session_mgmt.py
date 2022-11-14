from config import conn_mongodb
from datetime import datetime


class BlogSession:
    blog_page = {'A': 'blog_A.html', 'B': 'blog_B.html'}
    session_count = 0

    @staticmethod
    def save_session_info(session_ip, email, webpage_name):
        """사용자 Session 정보 저장"""
        now_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        mongo_db = conn_mongodb()
        mongo_db.insert_one({'session_ip': session_ip,
                             'email': email,
                             'page': webpage_name,
                             'access_time': now_time})

    @staticmethod
    def get_blog_page(blog_id=None):
        """Session 접속 횟수에 따른 블로그 화면 표시 변경"""
        if blog_id is not None:
            return BlogSession.blog_page[blog_id]
        if BlogSession.session_count == 0:
            BlogSession.session_count = 1
            return 'blog_A.html'
        else:
            BlogSession.session_count = 0
            return 'blog_B.html'
