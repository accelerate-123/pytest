#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time     : 2019/4/24 5:32 PM
# @Author   : dnie
# @Email    : niedi761@pingan.com.cn
# @File     : test_recharge.py
# @Software : PyCharm


import unittest
from homework_0423.common.contants import case_file
from homework_0423.common.doExcel import DoExcel
from homework_0423.common.doMysql import DoMySQL
from homework_0423.common.http_requests import HTTPRequest
from homework_0423.common.context import replace
from ddt import data, ddt
import json
from jsonpath import jsonpath
from homework_0423.common.mylog import MyLog

test_data = DoExcel(case_file, "recharge").getData()


@ddt
class TestFutureLoanRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.t=DoExcel(case_file,"recharge")
        cls.httpres=HTTPRequest()
        cls.mysql=DoMySQL()
        cls.logger=MyLog("test_recharge")

    @classmethod
    def tearDownClass(cls):
        cls.httpres.close()
        cls.mysql.close()

    @data(*test_data)
    def test_recharge(self,data_item):
        self.logger.info("==============================")
        self.logger.info("Execute No.{} testcase {}".format(data_item["case_id"],data_item["title"]))
        self.logger.info("Request Data is: {}".format(data_item))
        print(data_item["data"])
        if data_item["check_sql"] is not None:
            sql=json.loads(data_item["check_sql"])["sql"]
            before_amount=self.mysql.fetchone(sql)["leaveamount"]
            print("Before recharge, the price is {}".format(before_amount))
            res = self.httpres.send_requests(data_item["method"], data_item["url"], json.loads(data_item["data"]))
            try:
                self.assertEqual(data_item["expected"], jsonpath(res.json(), "$..msg")[0])
                testResult = "PASS"
                recharge_amount = int(eval(data_item["data"])['amount'])
                print("Recharge price is {}".format(recharge_amount))
                # sql = json.loads(data_item["check_sql"])["sql"]
                after_amount = self.mysql.fetchone(sql)["leaveamount"]
                print("After recharge, the price is {}".format(after_amount))
                self.assertEqual(int(before_amount) + recharge_amount, int(after_amount))
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