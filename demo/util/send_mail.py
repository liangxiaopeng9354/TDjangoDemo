#coding:utf-8
import smtplib
from email.mime.text import MIMEText
import importlib,sys

importlib.reload(sys)


print(sys.getdefaultencoding())


class SendEmail:


    global send_user
    global email_host
    global password
    email_host = "smtp.qq.com"
    send_user = "1435870361@qq.com"
    password = "kcptiwchwviubacc"

    def send_mail(self,user_list,sub,content):
        user = "liangxiaopeng"+"<" + send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)

        server.sendmail(user,user_list,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list,no_run):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        norun_num = float(len(no_run))
        count_num = pass_num + fail_num + norun_num

        pass_result = "%.2f%%" %(pass_num/count_num*100)
        fail_result = "%.2f%%" %(fail_num/count_num*100)
        user_list = ['liangxiaopeng@bjzjmy.com']
        sub = '接口自动化测试报告'
        content = '此次一共运行的接口个数为%s,通过个数为%s，失败个数为%s，没有运行的个数为%s,成功率为%s，失败率为%s' %(count_num,pass_num,fail_num,norun_num,pass_result,fail_result)
        self.send_mail(user_list,sub,content)





if __name__ == '__main__':
    sen = SendEmail()
    sen.send_main([1,2,3,4,5],[1,2,3,4])










