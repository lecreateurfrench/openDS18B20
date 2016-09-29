import sys
import os
import re
import getpass
import time
import subprocess
import Adafruit_DHT as dht
import file, mail, probe



FILES = []
SETTINGS = {"email":"","password":"","alert":{"choice": False, "max":0, "min":0}}
PROMPT = '> '


def to_float(array):
	floater = []
	for i in range(len(array)):
		floater.append(float(array[i]))
	return floater

def initialConfig():
	try: 
		path = os.path.abspath("/home/pi/ds18b20_conf")
		CONFIG = file.ConfigFile(path + "/config.json")
	except IOError:
		print "creating config.json in " + path
		try:
			os.makedirs(path)
		except OSError:
			print "already existing folder"
		subprocess.Popen(["touch", path + "/config.json"])
		time.sleep(1) #leaves enough time for the subprocess to create the file
		CONFIG = file.ConfigFile(path + "/config.json")
	return CONFIG
	
CONFIG = initialConfig()

def writeDependencies(file):
	print "before continuing you should add \"w1-gpio\" and \"w1-therm\" to /etc/modules files"
	return False

def promptConfig():
	print("adress where emails are going to be send and sent from ? ")
	SETTINGS["email"] = raw_input(PROMPT)
	print("password ? (warning the password will be kept clear in the config file)")
	SETTINGS["password"]= getpass.getpass()
	print("woud you like to set an alert system ?(y/n)")
	alert = raw_input(PROMPT)
	if str(alert) == "y": 
		SETTINGS["alert"]["choice"] = True
		print("max temp ?)")
		SETTINGS["alert"]["max"] = int(raw_input(PROMPT))
		print("min temp ?")
		SETTINGS["alert"]["min"] = int(raw_input(PROMPT))
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
			os.remove("/home/pi/ds18b20_conf/config.json")
			initialConfig()
			promptConfig()
			CONFIG.readData()
	elif CONFIG.nbline ==  0:
		promptConfig()
	CONFIG.readData()
	probes = probe.Probe()
	probes.detectProbe()
	dht_t, dht_h = dht.read_retry(dht.DHT22,17)
	try:		
		for p in range(len(probes.listprobes)):
			FILES.append(file.ProbeFile(probes.listprobes[p]))
			templine = FILES[p].readLine(2)
			probes.getTemperature(templine)
		
		email = mail.Mail()
		floater = to_float(probes.temperatures)
		if CONFIG.has_alert():
			if max(floater) >= CONFIG.getMaxTempAlert() or min(floater) <= CONFIG.getMinTempAlert():
				email.messageBody(probes.temperatures, True)
		else:		
			email.messageBody(probes.temperatures)
		probes.temperatures.append(str(dht_t))
		probes.temperatures.append(str(dht_h))
	except:
		print "temperatures couldn't be read : ", sys.exc_info()[0]
	try:
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



	

