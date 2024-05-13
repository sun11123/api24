import smtplib
# 发邮件
from email.mime.text import MIMEText
# 发送的对象
msg=MIMEText('邮件内容','plain','utf=8')
# 发件人
msg['From']='1137688913@qq.com'
# 收件人
msg['To']='1137688913@qq.com'
# 邮件主题
msg['Subject']='测试报告'

smtp=smtplib.SMTP_SSL('smtp.qq.com')
# 登录发件箱
smtp.login('1137688913@qq.com','drtochgtrmcajgii')
# 发送邮件
smtp.sendmail('1137688913@qq.com','1137688913@qq.com',msg.as_string())
smtp.quit()