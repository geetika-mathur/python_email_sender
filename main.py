import smtplib
import time
import sys

user = "Enter your username" # Enter your address
to =  "To address" # Enter receiver address
pwd = "Password" # Enter your password

server = smtplib.SMTP("smtp-mail.outlook.com", 587)
server.ehlo()
server.starttls()

try:
    subject = "testing"
    body = "successfully sent the email"
    message = 'From: ' + user + '\nSubject: ' + subject + '\n\n ' + body
except KeyboardInterrupt:
    print('\nCanceled')
    sys.exit()

try:
    server.login(user, pwd)
except smtplib.SMTPAuthenticationError:
    print('Your Username or Password is incorrect, please try again using the correct credentials')
    sys.exit()

try:
    server.sendmail(user, to, message)
    print('Successfully sent')
    time.sleep(.8)
except KeyboardInterrupt:
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\nThe username or password you entered is incorrect.')
    sys.exit()
except:
    print("Failed to Send")
server.close()
