import sys
import file, mail, probe
import subprocess 

config = file.ConfigFile("./config.json")
files = []
probes = probe.Probe()

def writeDependencies():
	file = file.File("/etc/modules")
	file.writeLine("w1-gpio")
	file.writeLine("w1-therm")
	subprocess.Popen(["sudo", "modprobe", "w1-gpio"])
	subprocess.Popen(["sudo", "modprobe", "w1-therm"])		
	

def promptConfig():


def main():
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
	for i range(len(files)):
		files[i].closeFile()
	return

if __name__ == '__main__':
	sys.exit(main())



	

