import sys
import os
import re
import getpass
import time
import subprocess
import file, mail, probe


def initialConfig():
	try: 
		CONFIG = file.ConfigFile("./config.json")
	except IOError:
		print "creation du fichier config.json"
		subprocess.Popen(["touch", "config.json"])
		time.sleep(1) #leaves enough time for the subprocess to create the file
		CONFIG = file.ConfigFile("./config.json")
	return CONFIG

FILES = []
SETTINGS = {"email":"","password":"","done":False}
PROMPT = '> '
CONFIG = initialConfig()

def writeDependencies(file):
	print "before continuing you should add \"w1-gpio\" and \"w1-therm\" to /etc/modules files"
	return False

def promptConfig():
	print("adress where emails are going to be send and sent from ? ")
	SETTINGS["email"] = raw_input(PROMPT)
	print("password ? (warning the password will be kept clear in the config file)")
	SETTINGS["password"]= getpass.getpass()
	SETTINGS["done"]=True
	CONFIG.register(SETTINGS)
	return 

def modulesTester():
	flag = [False, False]
	modules = file.ModuleFile("/etc/modules")
	for i in range(modules.nbline):
		line = modules.readLine(i+1)
		if re.match(r"^w1-gpio", line):
			flag[0] = True
		if re.match(r"^w1-therm", line):
			flag[1] = True
	if flag != [True, True]:
		return writeDependencies(modules)

	
	
def main():
	tester = modulesTester()
	if tester == False:
		return
	if len(sys.argv) > 1:
		if str(sys.argv[1]) == "erase":
			os.remove("./config.json")
			initialConfig()
			promptConfig()
			CONFIG.readData()
	elif CONFIG.nbline ==  0:
		promptConfig()
	CONFIG.readData()
	probes = probe.Probe()
	probes.detectProbe()
	try: 
		for p in range(len(probes.listprobes)):
			FILES.append(file.ProbeFile(probes.listprobes[p]))
			templine = FILES[p].readLine(2)
			probes.getTemperature(templine)
	except:
		print "temperatures couldn't be read : ", sys.exc_info()[0]
	try:
		email = mail.Mail()
		email.messageBody(probes.temperatures)
		email.credentials["email"], email.credentials["password"] = CONFIG.getCredentials()
		email.messageBuilder(email.credentials["email"], email.credentials["email"], "list of temperatures")
		email.sendMail()
	except:
		print "mail couldn't be send : ", sys.exc_info()[0]
	for i in range(len(FILES)):
		FILES[i].closeFile()
	CONFIG.closeFile()
	return

if __name__ == '__main__':
	sys.exit(main())



	

