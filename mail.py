#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
 
import smtplib  
from email.mime.text import MIMEText  
   
smtpHost = 'smtp.163.com' 
sender = 'jiuling_blockchain@163.com' 
password = "jiuLing0801"
receiver = '280507775@qq.com'
   
content = '您的状态为EXPIRED，请注意查看状态'
msg = MIMEText(content)  
   
msg['Subject'] = '主节点状态预警' 
msg['From'] = sender  
msg['To'] = receiver  
   
## smtp port 25
smtpServer = smtplib.SMTP(smtpHost, 25)         # SMTP
smtpServer.login(sender, password)
smtpServer.sendmail(sender, receiver, msg.as_string())  
smtpServer.quit()  
print 'send success by port 25'

## smtp ssl port 465
#smtpServer = smtplib.SMTP_SSL(smtpHost, 465)    # SMTP_SSL
#smtpServer.login(sender, password)  
#smtpServer.sendmail(sender, receiver, msg.as_string())  
#smtpServer.quit()  
#print 'send success by port 465'