#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/25 11:19 AM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : context.py
# @Software : PyCharm

from homework_0423.common.readconfig import ReadConfig
import re
from configparser import NoOptionError


class Context:
    mobile=None
    loan_id=None

def replace(data):
    p="#(.*?)#"
    while re.search(p,data):
        print(data)
        m=re.search(p,data)
        g=m.group(1)
        try:
            v=ReadConfig().getValue("data",g)
        except NoOptionError as e:
            if hasattr(Context,g):
                v=getattr(Context,g)
            else:
                print("Can't find this parameter.")
                raise e
        print(v)
        data=re.sub(p,v,data,count=1)
    return data

