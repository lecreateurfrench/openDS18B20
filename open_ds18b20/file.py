import json
import re

#from abc import ABCMeta, abstractmethod

class File(object):

	#__metaclass__ = ABCMeta

	#@abstractmethod
	def __init__(self, filepath):
		self.path = filepath
		self.file = open(self.path,"r")
		return

#	@abstractmethod
	def getContent(self):
		self.content = list(self.file)
		return self.content

#	@abstractmethod
	def nbLine(self):
		self.nbline = len(self.content)
		return self.nbline


#	@abstractmethod
	def readLine(self, nbline):
		return self.contenu[nbline-1]
	
#	@abstractmethod
	def closeFile(self):
		self.file.close()


class ConfigFile(File):
	
	def __init__(self, filepath):
	 	super(ConfigFile, self).__init__(filepath)
	 	self.data = json.load(self.file)

	def getCredentials(self):
	 	email = self.data["email"]
	 	password = self.data["password"]
	 	return email, password

	def closeFile(self):
	 	super(ConfigFile, self).closeFile()



class ProbeFile(File):

	def __init__(self, filepath):
		super(ProbeFile, self).__init__(filepath)

	def getContent(self):
		return super(ProbeFile, self).getContent()

	def nbLine(self):
		return super(ProbeFile, self).nbLine()


	def readLine(self, nbline):
		return super(ProbeFile, self).readLine(nbline)

	def closeFile(self):
		super(ProbeFile, self).closeFile()