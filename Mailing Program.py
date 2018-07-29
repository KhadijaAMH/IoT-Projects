import time
import os
import smtplib
import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import sys
gmail_user = "" #Enter Sender Mail Address here
gmail_pwd = ""  #Enter Sender Mail Password here
FROM = 'cbcbaby20@gmail.com'
TO = ['<enter mail address here'] #must be a list
msg = MIMEMultipart()
time.sleep(1)
msg['Subject'] ="testing msg send from python"
time.sleep(1)
fp = open("/home/pi/test.jpg", 'rb')
time.sleep(1)
img = MIMEImage(fp.read())
time.sleep(1)
fp.close()
time.sleep(1)
msg.attach(img)
time.sleep(1)
try:
	server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
	print "smtp.gmail"
	server.ehlo()
	print "ehlo"
	server.starttls()
	print "starttls"
	server.login(gmail_user, gmail_pwd)
	print "reading mail & password"
	server.sendmail(FROM, TO, msg.as_string())
	print "from"
	server.close()
	print 'successfully sent the mail'
		#GPIO.output(25, True)
		#time.sleep(2)
		#GPIO.output(25, False)

except:
	print "failed to send mail"
	
sys.exit(1)

