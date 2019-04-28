#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 2:44 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : mylog.py
# @Software : PyCharm

import logging
from homework_0423.common.contants import logpath


class MyLog:
    def __init__(self,log_name):
        self.log_name=log_name

    def my_log(self,msg,level):
        logger=logging.getLogger(self.log_name)
        logger.setLevel("DEBUG")

        formatter=logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")

        ch=logging.StreamHandler()
        ch.setLevel("DEBUG")
        ch.setFormatter(formatter)

        fh=logging.FileHandler(logpath,encoding="UTF-8")
        fh.setLevel("DEBUG")
        fh.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        if level=="DEBUG":
            logger.debug(msg)
        elif level=="INFO":
            logger.info(msg)
        elif level=="WARNING":
            logger.warning(msg)
        elif level=="ERROR":
            logger.error(msg)
        elif level=="CRITICAL":
            logger.critical(msg)

        logger.removeHandler(fh)
        logger.removeHandler(ch)


    def debug(self,msg):
        self.my_log(msg,"DEBUG")

    def info(self,msg):
        self.my_log(msg,"INFO")

    def warning(self,msg):
        self.my_log(msg,"WARNING")

    def error(self,msg):
        self.my_log(msg,"ERROR")

    def critical(self,msg):
        self.my_log(msg,"CRITICAL")


