# link to create app passwords https://myaccount.google.com/apppasswords"
import smtplib
import ssl

host = "smtp.gmail.com"
port = 465

username = "theflexfound@gmail.com"
password = "cekfmnjqvsfuohbf"

receiver = "awizomfashion@gmail.com"
message = """\
Subject: Hi!
Hello , 
how are you. 
Bye !"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )
