import threading
from bs4 import BeautifulSoup
import requests, datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

email_sender_account = "" #your email
email_sender_username = ""  #your email username
email_sender_password = ""#your email password
email_smtp_server = "" #change if not gmail.
email_smtp_port = 587 #change if needed.
email_recepients = ["xxx@gmail.com"] #your receipts
def SendEmail (text,time):
    email_subject = f"Reporting Text Changes at {time}"
    email_body = '<html><head></head><body>'
    email_body += '<style type="text/css"></style>' 
    email_body += f'<h2>Reporting Text Changes at {time}</h2>'
    email_body += f'<h1 style="color: rgb(86, 0, 251);">' 
    email_body += f'<b>Text</b>: ' 
    email_body += f'{text}</h1>' 
    server = smtplib.SMTP(email_smtp_server,email_smtp_port) 
    print(f"Logging in to {email_sender_account}")
    server.starttls() 
    server.login(email_sender_username, email_sender_password)
    for recipient in email_recepients:
        print(f"Sending email to {recipient}")
        message = MIMEMultipart('alternative') 
        message['From'] = email_sender_account 
        message['To'] = recipient 
        message['Subject'] = email_subject 
        message.attach(MIMEText(email_body, 'html')) 
        server.sendmail(email_sender_account,recipient,message.as_string())
    server.quit()

def printit():
  threading.Timer(10.0, printit).start()
  page = requests.get("")
  soup = BeautifulSoup(page.content, 'html.parser')
  text = soup.find_all('span')[0].get_text()
  TimeNow = datetime.datetime.now()
  if (text != 'This beta is full.' or text == '' or text != 'เบต้านี้เต็มแล้ว'):
      SendEmail(text,TimeNow)

printit()
