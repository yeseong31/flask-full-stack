import logging
# 파일로 남기기 위해서는 filename='test.log' 파라미터를 사용하고
# 어느 로그까지 남길 것인지는 level 로 설정 가능
logging.basicConfig(filename='test.log', level=logging.ERROR)

# 로그를 남길 부분에 다음과 같이 로그 레벨에 맞추어 출력해주면 해당 내용이 파일에 들어감
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
