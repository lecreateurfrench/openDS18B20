import json
import re

#from abc import ABCMeta, abstractmethod

class File(object):


	def __init__(self, filepath):
		self.path = filepath
		self.file = open(self.path,"r")

	def closeFile(self):
		self.file.close()


class ConfigFile(File):
	
	def __init__(self, filepath):
	 	super(ConfigFile, self).__init__(filepath)
	 	self.file = open(self.path,"r")
		
	def readData(self):
		self.data = json.load(self.file)

	def getCredentials(self):
	 	email = self.data["email"]
	 	password = self.data["password"]
	 	return email, password

	def is_done(self):
		if self.data["done"]== True:
			return True
		else:
			return False

	def register(self, settings):
		element = json.dumps(settings, indent=4)
		self._save(element)
		
	def _save(self, element):
		self.file = open(self.path, "w")
		self.file.write(element)
		self.file.close()
		self.file = open(self.path, "r")
	
	def closeFile(self):
	 	super(ConfigFile, self).closeFile()



class ProbeFile(File):

	def __init__(self, filepath):
		super(ProbeFile, self).__init__(filepath)
		self.content = list(self.file)
		self.nbline = len(self.content)

	def readLine(self, nbline):
		return self.content[nbline-1]

	def closeFile(self):
		super(ProbeFile, self).closeFile()

class ModuleFile(File):
	def __init__(self, filepath):
		super(ModuleFile, self).__init__(filepath)
		self.content = list(self.file)
		self.nbline = len(self.content)

	def readLine(self, nbline):
		return self.content[nbline-1]
	
	
	def closeFile(self):
		super(ModuleFile, self).closeFile()
	
