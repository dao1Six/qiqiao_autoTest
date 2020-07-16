import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_mail(filePath,sb):
    sender_mail = 'wujianlun@do1.com.cn'
    sender_pass = 'Wjl123456'
    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')


    # 邮件接受人信息
    # receivers = ['wujianlun@do1.com.cn','diaohuiyun@do1.com.cn','luolinyue@do1.com.cn','wangdongyi@do1.com.cn','wanghao2@do1.com.cn']
    receivers = ['wujianlun@do1.com.cn']
    # 邮件发送人，接收人设置
    msg_root['From'] = sender_mail
    msg_root['To'] = Header(",".join(receivers))
    # 邮件的主题，显示在接收邮件的预览页面
    subject = sb
    msg_root['subject'] = subject

    # 构造超文本  邮件正文
    content = MIMEText(str(open(filePath, 'rb').read(),'utf-8'),_subtype='html',_charset='utf-8')
    msg_root.attach(content)

    #html附件  邮件附件
    html = MIMEApplication(open(filePath, 'rb').read())
    html.add_header('Content-Disposition', 'attachment', filename="七巧测试报告附件.html")
    msg_root.attach(html)

    try:
        sftp_obj = smtplib.SMTP('smtp.exmail.qq.com')
        sftp_obj.login(sender_mail, sender_pass)
        sftp_obj.sendmail(sender_mail, receivers, msg_root.as_string())
        sftp_obj.quit()
        print('测试报告邮件发送成功！')

    except Exception as e:
        print('测试报告邮件发送失败！异常')
        print(e)

if __name__ == '__main__':
    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report\\result.html"
    send_mail(reportpath)