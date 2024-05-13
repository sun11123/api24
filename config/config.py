import logging
import os

prj_path=os.path.dirname(os.path.abspath(__file__))
test_path=os.path.join(prj_path,'test')
data_path=os.path.join(prj_path,"data")
log_file=os.path.join(prj_path, '../log/log.txt')
report_file=os.path.join(prj_path, '../report/report.html')
data_file=os.path.join(prj_path,"data",'test_user_data.xlsx')

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s:%(name)s:%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='../log/log.txt',
                    filemode='a')

# 数据库配置
db_host='127.0.0.1'
db_port=3306
db_user='root'
db_password='root'
db='xzs'

# 邮件配置
smtp_server='smtp.qq.com'
smtp_user='2463926466@qq.com'
smtp_ps='soyhmrbalutoebaf'
sender=smtp_user
receiver='2463926466@qq.com'
subject='接口测试报告'

if __name__ == '__main__':
   logging.info("接口测试")


