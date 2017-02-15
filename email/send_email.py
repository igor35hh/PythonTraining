import smtplib
import base64

host = "mail.svcorp.com.ua"
port = 25
username = "info1c@svcorp.com.ua"
password = "123"
from_email = username
to_list = ["Klimets@svcorp.com.ua"]
filename = 'order_1.pdf'

marker = "AUNIQUEMARKER"
body   = "Hello! there is an email message"

fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)
nameUser = "".format("Igor")

part1 = """From: From The Online Shop <>
To: To """+nameUser+""" <>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multipart/mixed; boundary=%s
--%s
""" % (marker, marker)

part2 = """Content-Type: text/plain
Content-Transfer-Encoding:8bit

%s
--%s
""" % (body,marker)

part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)

message = part1 + part2 + part3

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
email_conn.sendmail(from_email, to_list, message)
email_conn.quit()
