import smtplib


sender = ""  # login account
password = ""  # password account

receiver = ""
subject = "Python email test"  # title message
body = "I wrote an email with Python :D"

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

# message = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (sender, receiver, subject, body)

server = smtplib.SMTP("smtp.yandex.ru", 587)
server.starttls()


try:
    server.login(sender, password)
    print("Logged in...")
    server.sendmail(sender, receiver, message)
    print("Email has been sent!")
except smtplib.SMTPAuthenticationError:
    print("Unable to sign in")
