# coding=utf-8
'''
@author: Angie

@desc: 发送报告邮件

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time, os


# =============定义发送邮件==========
# SMTP服务器
SmtpServer = 'smtp.126.com'
# 发信邮箱
Sender = ''
AuthCode = ''
# 收信邮箱
Receiver = ['']
def send_mail(file_new,mailto):
    # 定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header('接口测试报告', 'utf-8')
    msg['From'] = Sender
    msg['To'] = ",".join(mailto)
    # 定义发送时间
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器
    smtp.connect(SmtpServer)
    smtp.login(Sender, AuthCode)
    smtp.sendmail(Sender, mailto, msg.as_string())
    smtp.quit()
    print 'email has send out !'

# ======查找测试报告目录，找到最新生成的测试报告文件====
def send_report(report_path):
    lists = os.listdir(report_path)
    lists.sort(key=lambda fn: os.path.getmtime(report_path + "\\" + fn))
    # 找到最新生成的报告文件
    file_new = os.path.join(report_path, lists[-1])
    print file_new
    # 调用发邮件函数
    send_mail(file_new, Receiver)