"""
自定义日志
1、控制台输出
2、运行过程中输出日志到文件
3、
"""

import logging
import os.path

logger = logging.getLogger("weixin")
logger.setLevel(logging.DEBUG)
""""
Formatter() 定义日志格式

"""
formatter = logging.Formatter("%(asctime)s%(levelname)s%(message)s")

"""
StreamHandler() 控制台输出处理器

"""
sh = logging.StreamHandler()

sh.setFormatter(formatter)

sh.setLevel(logging.DEBUG)

# 添加控制台输出
logger.addHandler(sh)

"""
添加日志文件路径
"""
logs = os.path.join(os.path.dirname(__file__), "../logs")
if not os.path.exists(logs):
    os.mkdir(logs)
logfile = os.path.join(logs, "weixin.log")
fh = logging.FileHandler(logfile)
fh.setFormatter(formatter)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

if __name__ == "__main__":
    logger.info("this is test")
