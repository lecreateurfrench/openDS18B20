import sys
import re
import getpass
import file, mail, probe

config = file.ConfigFile("./config.json")
files = []
settings = {"email":"","password":"","done":False}
prompt = '> '

def writeDependencies(file):
	print "before continuing you should add \"w1-gpio\" and \"w1-therm\" to /etc/modules files"
	return False

def promptConfig():
	print("adress where emails are going to be send and sent from ? ")
	settings["email"] = raw_input(prompt)
	print("password ? (warning the password will be kept clear in the config file)")
	settings["password"]= getpass.getpass()
	settings["done"]=True
	config.register(settings)
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
	config.readData()
	if config.is_done() != True:
		promptConfig()
	probes = probe.Probe()
	probes.detectProbe()
	for p in range(len(probes.listprobes)):
		files.append(file.ProbeFile(probes.listprobes[p]))
		templine = files[p].readLine(2)
		probes.getTemperature(templine)
	email = mail.Mail()
	email.messageBody(probes.temperatures)
	email.credentials["email"], email.credentials["password"] = config.getCredentials()
	email.messageBuilder(email.credentials["email"], email.credentials["email"], email.body)
	email.sendMail()
	for i in range(len(files)):
		files[i].closeFile()
	config.closeFile()
	return

if __name__ == '__main__':
	sys.exit(main())



	

