#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Email():

	def __init__(self):
		self.credentials = { "email": "", "password": ""}
		self.msg = MIMEMultipart() 
		self.body = ""
		return 

	def sendmail(self,smtp_server="smtp.gmail.com", port=587, toaddr):

		self.msg.attach(MIMEText(self.body,'plain'))
		text = self.msg.as_string()
		server=smtplib.SMTP(smtp_server,port)
		server.starttls()
		server.login(self.credentials["email"], self.credentials["password"])
		server.sendmail(self.msg["From"], self.msg["To"], text)
		server.quit()
		return

	def getCredentials(self,credentials):
		self.credentials["email"] = credentials[0]
		self.credentials["password"] = credential[1]
		return self.credentials

	def messageBody(self,temperatures):
		i = 0
		self.body = "Voici la listes des températures\n"
		for temperature in temperatures:
			self.body += "sonde " + i + " : " + temperature + " C\n"
		return self.body

	def messagebuilder(toaddr, fromaddr, subject):
		self.msg["From"] = fromaddr
		self.msg["To"] = toaddr
		self.msg["Subject"] = subject
		return self.msg




