# coding=utf-8
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(filePath):
    """

    :param title:
    """
    try:
        #发送人信息
        sender ="wujianlun@do1.com.cn"
        server = smtplib.SMTP('smtp.exmail.qq.com')
        server.login("wujianlun@do1.com.cn", "Wjl123456")
        #接受人信息
        receivers = ['wujianlun@do1.com.cn']
        receiver = ','.join(receivers)

        htmlf = open(filePath, 'r', encoding="utf-8")
        msg = MIMEText(htmlf.read(), 'html', 'utf-8')
        msg['To'] = receiver
        msg['Subject'] = '七巧测试报告'  # 邮件主题
        msg['From'] = 'wujianlun@do1.com.cn'  # 发送者账号
        # 邮件正文

        # 构造附件1
        # att1 = MIMEText(open(filePath, 'rb').read(), 'base64', 'utf-8')
        # att1['Content-Type'] = 'application/octet-stream'
        # att1['Content-Disposition'] = 'attachment; filename= "report.html"'
        # msg.attach(att1)




        server.sendmail(sender, receiver, msg.as_string())
        server.close ()
        print('测试报告邮件发送成功！')

    except Exception as msg:
        print('测试报告邮件发送失败！异常：%s' % msg)



if __name__ == '__main__':
    ProjectRootPath = os.getcwd().split('qiqiao_autoTest')[0] + "qiqiao_autoTest"
    # 报告目录
    reportpath = ProjectRootPath + "\\report\\测试报告.html"
    send_mail(reportpath)
