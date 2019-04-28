#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 1:56 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : readconfig.py
# @Software : PyCharm


from configparser import ConfigParser
from homework_0423.common.contants import global_conf, online_conf, test_conf


class ReadConfig:
    def __init__(self,encoding="utf-8"):
        self.cf=ConfigParser()
        self.cf.read(global_conf,encoding)
        switch=self.cf.getboolean("switch","on")
        if switch:
            self.cf.read(online_conf,encoding)
        else:
            self.cf.read(test_conf,encoding)

    def getValue(self,sections,options):
        return self.cf.get(sections,options)

