from flask import Flask

app = Flask(__name__)

app.debug = False
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler # logging 핸들러 이름을 적어줌
    file_handler = RotatingFileHandler('test_log.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING) # 어느 단계까지 로깅을 할지를 적어줌
    app.logger.addHandler(file_handler) # app.logger.addHandler() 에 등록


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return "<h1>404 Error</h1>해당 경로에 맞는 웹페이지가 없습니다.", 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
