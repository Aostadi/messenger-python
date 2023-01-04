import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import smtplib


class send_email:
    def __init__(self, email):
        self.__email = email

    def send_code(self):
        try:
            msg = MIMEMultipart()
            email = self.__email
            password = "cvjypaucrwhzzyhl"
            msg['From'] = "pybot.com@gmail.com"
            code = random.randint(1000, 9000)
            msg['To'] = self.__email
            msg['Subject'] = 'verify email'
            message = f'''**************** Hello
            your verfiaction code is {code}'''
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())
            print(
                '********* we had send you a verfiaction code (please check your spam folder)')
            verify = input('''*********** Please enter your verify code
            (if you want to send another code or exit  press enter) : ''')
            if verify == '' or verify != code:
                choice = input('1.send other code 2.exit ; Enter menu number : ')
                if choice == '1':
                    send_email.send_code(email)
                else:
                    exit()
        except:
            print('sth went wrong')

    def sucess(self, title):
        try:
            time = datetime.datetime.now()
            msg = MIMEMultipart()
            password = "cvjypaucrwhzzyhl"
            msg['From'] = "pybot.com@gmail.com"
            msg['To'] = self.email
            msg['Subject'] = f'sucessfull {title}'
            message = f'''**************** Hello
            you are sucessfully {title} at {time.year} / {time.month} / {time.day} {time.hour} : {time.minute} : {time.second}'''
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()

            server.login(msg['From'], password)

            server.sendmail(msg['From'], msg['To'], msg.as_string())
        except:
            print(" can't send sucses mail")
