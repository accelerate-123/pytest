#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 11:35 AM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : http_requests.py
# @Software : PyCharm

import requests



class HTTPRequest:
    def __init__(self):
        self.session=requests.session()
        self.header={"Content-Type":"application/json"}

    def send_requests(self,method,url,param):
        if method.upper()=="GET":
            try:
                res=self.session.request(method=method,url=url,params=param)
            except Exception as e:
                print("Send GET Request error, The Error is {}".format(e))
                raise e
        elif method.upper()=="POST":
            try:
                res=self.session.request(method=method,url=url,data=param)
            except Exception as e:
                print("Send POST Request error, The Error is {}".format(e))
                raise e
        else:
            print("Send Request error, The Error is {}".format(e))
        return res

    def close(self):
        self.session.close()

