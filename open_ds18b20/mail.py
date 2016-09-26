#!/usr/bin/python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email():

	def __init__(self):
		self.credentials = { "email": "", "password": ""}
		self.msg = MIMEMultipart() 
		self.body = ""
		return 

	def sendmail(self,smtp_server="smtp.gmail.com", port=587):
		self.msg.attach(MIMEText(self.body,'plain'))
		text = self.msg.as_string()
		server=smtplib.SMTP(smtp_server,port)
		server.starttls()
		server.login(self.credentials["email"], self.credentials["password"])
		server.sendmail(self.msg["From"], self.msg["To"], text)
		server.quit()
		return

	#def getCredentials(self,credentials):
	#	self.credentials["email"] = credentials[0]
	#	self.credentials["password"] = credential[1]
	#	return self.credentials

	def messageBody(self,temperatures):
		self.body = "Voici la listes des temperatures\n"
		for i in range(len(temperatures)):
			self.body += "sonde " + i + " : " + temperatures[i] + "*C\n"
		return self.body

	def messagebuilder(self, toaddr, fromaddr, subject):
		self.msg["From"] = fromaddr
		self.msg["To"] = toaddr
		self.msg["Subject"] = subject
		return self.msg




