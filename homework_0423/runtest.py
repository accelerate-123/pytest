#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/26 9:46 AM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : runtest.py
# @Software : PyCharm

import sys
sys.path.append('./')

from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest
from homework_0423.common.contants import testdir, report_name


discover=unittest.defaultTestLoader.discover(testdir,pattern="test_*")

if __name__=="__main__":
    with open(report_name,"wb") as f:
        runner=HTMLTestRunner(stream=f,title="前程贷接口自动化测试",description="接口执行结果")
        runner.run(discover)

