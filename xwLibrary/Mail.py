#!/usr/bin/env python
#coding=utf-8

'''
    mail = Mail_class.mail('smtp.exmail.qq.com',465,'it@huomaotv.com','VFboAvxK3A^qg%zl',['xiawei@huomaotv.com','xiongyunfeng@huomaotv.com'])
    mail.send_mail("hello","<a href='http://huomaotv.cn'>火猫</a>")
'''

class mail:

    #收件箱
    mailto_list=''

    #设置服务器
    mail_host=''

    #设置服务器端口
    mail_port=465

    #发件邮箱
    mail_user=''

    #密码
    mail_pass=''


    # @mail_host : string 设置服务器
    # @mail_port : int 设置服务器端口
    # @mail_user : string 发件邮箱
    # @mailto_list : list 收件箱
    def __init__(self,mail_host,mail_port,mail_user,mail_pass,mailto_list):
        self.mail_host = mail_host
        self.mail_port = mail_port
        self.mail_user = mail_user
        self.mail_pass = mail_pass
        self.mailto_list = mailto_list


    # @sub : string 主题
    # @content : string 邮件内容
    def send_mail(self,sub,content):

        import smtplib
        from email.mime.text import MIMEText

        #这里的hello可以任意设置，收到信后，将按照设置显示
        #me=self.mail_user
        me="系统发送"+"<"+self.mail_user+">"

        #创建一个实例，这里设置为html格式邮件
        msg = MIMEText(content,_subtype='html',_charset='utf-8')

        #设置主题
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(self.mailto_list)

        try:
            #注意！如果是使用SSL端口，这里就要改为SMTP_SSL
            s = smtplib.SMTP_SSL(self.mail_host, self.mail_port)
            #登陆服务器
            s.login(self.mail_user,self.mail_pass)
            #发送邮件
            s.sendmail(me, self.mailto_list, msg.as_string())
            s.close()
            return True
        except Exception, e:
            print str(e)
            return False
