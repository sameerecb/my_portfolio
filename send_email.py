# link to create app passwords https://myaccount.google.com/apppasswords"
import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "theflexfound@gmail.com"
    password = "cekfmnjqvsfuohbf"

    receiver = "awizomfashion@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
