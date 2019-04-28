#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 1:42 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : doMysql.py
# @Software : PyCharm


import pymysql
from homework_0423.common.readconfig import ReadConfig


class DoMySQL:
    def __init__(self):
        db_host=ReadConfig().getValue("data","db_host")
        db_user=ReadConfig().getValue("data","db_user")
        db_pwd=ReadConfig().getValue("data","db_pwd")
        db_port=ReadConfig().getValue("data","db_port")
        self.mysql=pymysql.connect(host=db_host,user=db_user,password=db_pwd,port=int(db_port),charset="utf8")
        self.cursor=self.mysql.cursor(pymysql.cursors.DictCursor)

    def fetchone(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchone()

    def fetchall(self,sql):
        self.cursor.execute(sql)
        self.mysql.commit()
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.mysql.close()

