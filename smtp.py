# -*- coding: UTF-8 -*-

from smtplib import SMTP_SSL
from time import sleep
from email.mime.text import MIMEText
from email.utils import formataddr

from_addr = 'xxxxxxxxxxx@qq.com'  #发件人邮箱
to_addr = 'xxxxxxxxxxx@qq.com'  #收件人邮箱
username = 'xxxxxxxx'
password = 'xxxxxxxx'


def s_mail():
	ret = True
	try:
		msg=MIMEText('填写邮件内容','plain','utf-8')
		msg['From']=formataddr(["发件人昵称",from_addr])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
		msg['To']=formataddr(["收件人昵称",to_addr])              # 括号里的对应收件人邮箱昵称、收件人邮箱账号
		msg['Subject']="邮件主题-测试"                # 邮件的主题，也可以说是标题

		server=SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
		server.login(username, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
		server.set_debuglevel(1)
		server.sendmail(from_addr,[to_addr,],msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
	except Exception: # 如果 try 中的语句没有执行，则会执行下面的 ret=False
		ret=False
	return ret


ret=s_mail()

if ret:
	print("success")
else:
	print("Fail")
