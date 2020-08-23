#smtp library 

import smtplib 
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)  #define server
#server.connect("smtp.example.com", 587)

server.ehlo() #start process
server.starttls()
server.ehlo()
server.login('your email here', 'your password here') #login

#specify headers 
msg = MIMEMultipart() 
msg['From'] = 'your name here'
msg['To'] = 'someemailhere' 
msg['Subject'] = 'Hello!' 

with open('message.text', 'r') as f: 
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

#attach an image
filename = 'hello.jpg'
attachment = open(filename, 'rb')

#create payload 
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

#encoders 
encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachement; filename = {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('your email here', 'recipient here', text)
server.quit()