import smtplib  
from email.mime.text import MIMEText
from email.header import Header

def send_email(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()

send_email('smtp.163.com', 'jiuling_blockchain@163.com', 'jiuLing0801', '280507775@qq.com', 'hello', 'hello')