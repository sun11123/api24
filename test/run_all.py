import logging
import unittest
from lib.HTMLTestRunner import HTMLTestRunner
from lib.send_email import send_email
from config.config import *

def discover():
    return unittest.defaultTestLoader.discover(test_case_path,'test*.py')

def run(suit):
    logging.info("=========开始测试=========")
    with open(report_file,'wb') as f:
           HTMLTestRunner(
               stream=f,
               title='xzs测试用例',
               description='xzs的登录和注册',
               verbosity=2
           ).run(suit)
    logging.info("=========测试结束=========")

def run_suite(suite_name):
    suite=get_suit(suite_name)
    if isinstance(suite,unittest.TestSuite):
        run(suite)
    else:
        print("TestSuite不存在")
def run_all():
    run(discover())

if __name__=='__main__':
    run_all()


