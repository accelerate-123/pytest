#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/25 3:05 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : test_invest.py
# @Software : PyCharm


import unittest
from homework_0423.common.contants import case_file
from homework_0423.common.doExcel import DoExcel
from homework_0423.common.doMysql import DoMySQL
from homework_0423.common.http_requests import HTTPRequest
from homework_0423.common.context import replace, Context
from ddt import data, ddt
import json
from jsonpath import jsonpath
from homework_0423.common.mylog import MyLog

test_data = DoExcel(case_file, "invest").getData()


@ddt
class TestFutureLoanInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=DoExcel(case_file,"invest")
        cls.httpres=HTTPRequest()
        cls.mysql=DoMySQL()
        cls.logger=MyLog("test_invest")

    @classmethod
    def tearDownClass(cls):
        cls.httpres.close()
        cls.mysql.close()

    @data(*test_data)
    def test_invest(self,data_item):
        self.logger.info("==============================")
        self.logger.info("Execute No.{} testcase {}".format(data_item["case_id"],data_item["title"]))
        self.logger.info("Request Data is: {}".format(data_item))
        print(data_item["data"])
        if data_item["check_sql"] is not None:
            data_item["data"] = replace(data_item["data"])
            sql=json.loads(data_item["check_sql"])["sql"]
            loan_id=self.mysql.fetchone(sql)["id"]
            print("标的ID",loan_id)
            setattr(Context,"loan_id",str(loan_id))
            res=self.httpres.send_requests(data_item["method"],data_item["url"],json.loads(data_item["data"]))
            try:
                self.assertEqual(data_item["expected"], jsonpath(res.json(), "$..msg")[0])
                testResult = "PASS"
            except Exception as e:
                self.logger.error("Execute testcase failed. {}".format(e))
                testResult = "FAILED"
                raise e
            finally:
                self.logger.info("=============Begin write data============")
                self.t.writeData(data_item["case_id"] + 1, 7, jsonpath(res.json(), "$..msg")[0])
                self.t.writeData(data_item["case_id"] + 1, 8, testResult)
                self.logger.info("=============End write data============")
        else:
            data_item["data"] = replace(data_item["data"])
            res = self.httpres.send_requests(data_item["method"], data_item["url"], json.loads(data_item["data"]))
            try:
                self.assertEqual(data_item["expected"], jsonpath(res.json(), "$..msg")[0])
                testResult = "PASS"
            except Exception as e:
                self.logger.error("Execute testcase failed. {}".format(e))
                testResult = "FAILED"
                raise e
            finally:
                self.logger.info("=============Begin write data============")
                self.t.writeData(data_item["case_id"] + 1, 7, jsonpath(res.json(), "$..msg")[0])
                self.t.writeData(data_item["case_id"] + 1, 8, testResult)
                self.logger.info("=============End write data============")



if __name__=="__main__":
    unittest.main()