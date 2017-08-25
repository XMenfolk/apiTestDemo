# coding=utf-8
'''
@author: Angie

@desc: 发送报告邮件

'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import time, os


# =============定义发送邮件==========
# SMTP服务器
SmtpServer = 'smtp.126.com'
# 发信邮箱
Sender = 'xautotest@126.com'
AuthCode = 'test918'
# 收信邮箱
Receiver = ['wealthboss@163.com']

def sendMail(fileNew, mailto):
    """
    发送邮件
    """
    # 定义正文
    f = open(fileNew, 'rb')
    mailBody = f.read()
    #msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    htmlBody = MIMEText(mailBody, _subtype='html', _charset='utf-8')
    f.close()
    # 构造附件
    att = MIMEText(open(fileNew,'rb').read(),'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment; filename="接口测试报告.html"'
    msg = MIMEMultipart('alternative')
    msg.attach(htmlBody)
    msg.attach(att)
    # 定义标题
    msg['Subject'] = Header('测试报告', 'utf-8').encode()
    msg['From'] = Sender
    msg['To'] = ",".join(mailto)
    # 定义发送时间
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp = smtplib.SMTP()
    # 连接 SMTP 服务器
    smtp.connect(SmtpServer)
    # 用户名密码
    smtp.login(Sender, AuthCode)
    smtp.sendmail(Sender, mailto, msg.as_string())
    smtp.quit()
    print 'email has send out !'


# ======查找测试报告目录，找到最新生成的测试报告文件====
def sendReport(reportPath):
    """
    查找最新测试报告，调用发送邮件函数
    """
    # result_dir = report_path
    lists = os.listdir(reportPath)
    lists.sort(key=lambda fn: os.path.getmtime(reportPath + "\\" + fn))
    # print (u'最新测试生成的报告： '+lists[-1])
    # 找到最新生成的文件
    fileNew = os.path.join(reportPath, lists[-1])
    print fileNew
    # 调用发邮件模块
    sendMail(fileNew, Receiver)
