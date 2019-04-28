#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 1:42 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : contants.py
# @Software : PyCharm


import os, time

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

case_file=os.path.join(base_dir,"test_data","cases.xlsx")
global_conf=os.path.join(base_dir,"conf","global.conf")
online_conf=os.path.join(base_dir,"conf","online.conf")
test_conf=os.path.join(base_dir,"conf","test.conf")

testdir=os.path.join(base_dir,"testcases")
reportdir=os.path.join(base_dir,"reports")
logdir=os.path.join(base_dir,"logs")

now=time.strftime("%Y-%m-%d")
logpath=os.path.join(logdir,"test_api_"+now+".txt")
report_name=reportdir+"/testcase_"+now+".html"