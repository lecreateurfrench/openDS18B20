import json
import re


class File():

	def __init__(self, path):
		self.path = path
		self.file = open(path,"r")
		return

	def getContent(self):
		return(self.content = list(self.file))

	def nbLine(self):
		return(self.nbline = len(self.content))


	def readLine(self, nbline)
		return self.contenu[nbline-1]

	def closeFile(self):
		self.file.close()


class ConfigFile(File):
	
	def __init__(self, path):
	 	super.__init__(self, path)
	 	self.data = json.load(self.file)

	 def getCredentials(self):
	 	email = self.data["email"]
	 	password = self.data["password"]
	 	return email, password

	 def closeFile(self):
	 	super.closeFile(self)



class ProbeFile(File):

	def __init__(self,path):
		super.__init__(self.path)

	def getContent(self):
		return super.getContent(self)

	def nbLine(self):
		return super.nbLine(self)


	def readLine(self, nbline)
		return super.readLine(self, nbline)

	def closeFile(self):
		super.closeFil(self)