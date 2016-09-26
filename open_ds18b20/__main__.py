import sys
from openDS18b20 import file, email, probe

config = file.FileConfig("config.json")
files = []
probes = probe.Probe()



def main():
	probe.detectProbe()
	for p in range(len(probe.listprobes)):
		files.append(file.ProbeFile(listprobes))
		templine = files[p].readline(2)
		probes.getTemperatures(templine)
	mail = email.Email()
	mail.messageBody(probes.temperatures)
	mail.credentials["email"], mail.credentials["password"] = config.getCredentials()
	mail.messageBuilder(mail.credentials["email"], mail.credentials["email"], mail.body)
	mail.sendMail()
	return

if __name__ == '__main__'
	sys.exit(main())



	

