import os
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_HtmlFileEmail(filePath,subject):
    '''发送携带Html文件的邮件'''
    sender_mail = 'wujianlun@do1.com.cn'  #发送者邮箱地址
    sender_pass = 'Wjl123456' #发送者邮箱密码
    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed') #一封邮件由以下几部分组成：
    # {邮件发送人、邮件接受人信息、邮件标题、邮件正文、邮件附件}

    # 邮件发送人
    msg_root['From'] = sender_mail
    # 邮件接受人信息
    receivers = ['wujianlun@do1.com.cn']
    msg_root['To'] = Header(",".join(receivers))
    # 邮件标题
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

def send_TextEmail(subject,text_info ):
    '''发送普通文本邮件'''
    sender_mail = 'wujianlun@do1.com.cn'  # 发送者邮箱地址
    sender_pass = 'Wjl123456'  # 发送者邮箱密码
    # 设置总的邮件体对象，对象类型为mixed
    msg_root = MIMEMultipart('mixed')  # 一封邮件由以下几部分组成：
    # {邮件发送人、邮件接受人信息、邮件标题、邮件正文、邮件附件}

    # 邮件发送人
    msg_root['From'] = sender_mail
    # 邮件接受人信息
    receivers = ['wujianlun@do1.com.cn']
    msg_root['To'] = Header(",".join(receivers))
    # 邮件标题
    msg_root['subject'] = subject
    # 构造超文本  邮件正文
    content = MIMEText(text_info,'plain', 'utf-8')
    msg_root.attach(content)
    try:
        sftp_obj = smtplib.SMTP('smtp.exmail.qq.com')
        sftp_obj.login(sender_mail,sender_pass)
        sftp_obj.sendmail(sender_mail,receivers,msg_root.as_string())
        sftp_obj.quit()
        print('测试报告邮件发送成功！')
    except Exception as e:
        print('测试报告邮件发送失败！异常')
        print(e)

if __name__ == '__main__':
    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report\\result.html"
    send_HtmlFileEmail(reportpath)