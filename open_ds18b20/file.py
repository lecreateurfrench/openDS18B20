import json
import re

#from abc import ABCMeta, abstractmethod

class File(object):

	#__metaclass__ = ABCMeta

	#@abstractmethod
	def __init__(self, filepath):
		self.path = filepath
		self.file = open(self.path,"r")


#	@abstractmethod
	def readLine(self, nbline):
		return self.content[nbline-1]
	
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
		self.content = list(self.file)
		self.nbline = len(self.content)

	def readLine(self, nbline):
		return super(ProbeFile, self).readLine(nbline)

	def closeFile(self):
		super(ProbeFile, self).closeFile()
