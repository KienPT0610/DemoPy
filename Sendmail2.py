import yagmail
import getpass

#Login
password = getpass.getpass('Nhap PASS: ')
yag = yagmail.SMTP("fbkienpt@gmail.com", password=password)

fi = open(r'DSMail.txt', encoding='utf8')
to = []
r = fi.read().split()
to.append(r)
subject = "Xin Chao!"
body = '''
Test
'''
file_path = ["Sendmail2.py"]
for _ in range(len(to)):
    yag.send(to=to[_], subject=subject, contents=body, attachments=file_path)
print('Success!')