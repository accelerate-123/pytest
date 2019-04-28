#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 2:36 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : test_register.py
# @Software : PyCharm


import unittest
from homework_0423.common.http_requests import HTTPRequest
from homework_0423.common.contants import case_file
from homework_0423.common.doMysql import DoMySQL
from homework_0423.common.doExcel import DoExcel
from homework_0423.common.mylog import MyLog
from homework_0423.common.context import Context
from ddt import ddt, data
import json
from jsonpath import jsonpath


test_data=DoExcel(case_file,"register").getData()
print(test_data)

@ddt
class TestFutureLoanRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.httpres=HTTPRequest()
        cls.mysql=DoMySQL()
        cls.logger=MyLog("test_register")
        cls.t=DoExcel(case_file,"register")

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
        cls.httpres.close()

    @data(*test_data)
    def test_register(self,data_item):
        self.logger.info("=================================")
        self.logger.info("Execute No. {} testcase {}".format(data_item["case_id"],data_item["title"]))
        self.logger.info("Request Data is {}".format(data_item))
        if data_item["check_sql"] is not None:
            sql=json.loads(data_item["check_sql"])["sql"]
            before=self.mysql.fetchone(sql)["num"]
            res=self.httpres.send_requests(data_item["method"],data_item["url"],json.loads(data_item["data"]))
            try:
                self.assertEqual(data_item["expected"],jsonpath(res.json(),"$..msg")[0])
                testResult="PASS"
                after=self.mysql.fetchone(sql)["num"]
                print(after)
                self.assertEqual(int(before)+1,int(after))
            except Exception as e:
                self.logger.error("Execute testcase failed. {}".format(e))
                testResult = "FAILED"
                raise e
            finally:
                self.logger.info("=============Begin write data============")
                self.t.update_init_data(self.t.get_init_data() + 1)
                self.t.writeData(data_item["case_id"]+1,7,jsonpath(res.json(),"$..msg")[0])
                self.t.writeData(data_item["case_id"]+1,8,testResult)
                self.logger.info("=============End write data============")
        else:
            res=self.httpres.send_requests(data_item["method"],data_item["url"],json.loads(data_item["data"]))
            try:
                self.assertEqual(data_item["expected"],jsonpath(res.json(),"$..msg")[0])
                testResult="PASS"
            except Exception as e:
                self.logger.error("Execute testcase failed. {}".format(e))
                testResult = "FAILED"
                raise e
            finally:
                self.logger.info("=============Begin write data============")
                self.t.writeData(data_item["case_id"]+1,7,jsonpath(res.json(),"$..msg")[0])
                self.t.writeData(data_item["case_id"]+1,8,testResult)
                self.logger.info("=============End write data============")

if __name__=="__main__":
    unittest.main()