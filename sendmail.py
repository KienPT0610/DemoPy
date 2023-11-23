import smtplib
import getpass

#Code by Kien PT
email = 'fbkienpt@gmail.com'
password = getpass.getpass('Nhap password email: ')
print('Mail to: ')
email_sent = input()
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls() #bat bao mat cua gmail
session.login(email, password)
mail_content = '''Subject: Xin Chao Thu Trang!
Anh vua code ra con app auto gui mail nen anh test thu
From: Pham Trung Kien
-------------------------------------------------------------
'''
session.sendmail(email, email_sent, mail_content)
print('mail sent')




