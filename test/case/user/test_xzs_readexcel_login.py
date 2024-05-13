import json
import unittest,requests
from read_excel import *
from db import *
from config import *


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li=read_excel().excel_to_list("../../test_user_data.xlsx", "test_user_reg")
    def test_reg_ok(self):
        case_data=read_excel().get_test_data(self.li,'reg_ok')
        url=case_data.get('url')
        args= case_data.get('args')
        a=json.loads(args).get("userName")
        expect_res = case_data.get('expect_res')
        if check_user(name=a):
            del_user(a)
        res = requests.post(url=url, json=json.loads(args))
        logging.info("测试用例：{}".format('test_reg_ok'))
        logging.info("url:{}".format(url))
        logging.info("请求参数：{}".format(args))
        logging.info("期望结果：{}".format(expect_res))
        logging.Logger("实际结果：{}".format(res.text))
        self.assertIn(expect_res,res.text)

    def test_reg_err(self):
        case_data=read_excel().get_test_data(self.li,'reg_err')
        url = case_data.get('url')
        args = case_data.get('args')
        expect_res = case_data.get('expect_res')
        res = requests.post(url=url, json=json.loads(args))
        logging.info("测试用例：{}".format('test_reg_err'))
        logging.info("url:{}".format(url))
        logging.info("请求参数：{}".format(args))
        logging.info("期望结果：{}".format(expect_res))
        logging.Logger("实际结果：{}".format(res.text))
        self.assertIn(expect_res, res.text)

if __name__ == '__main__':
    unittest.main()
