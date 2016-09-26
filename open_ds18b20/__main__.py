import sys
import file, mail, probe

config = file.ConfigFile("./config.json")
files = []
probes = probe.Probe()



def main():
	probes.detectProbe()
	for p in range(len(probe.listprobes)):
		files.append(file.ProbeFile(listprobes))
		templine = files[p].readline(2)
		probes.getTemperatures(templine)
	mail = mail.Mail()
	mail.messageBody(probes.temperatures)
	mail.credentials["email"], mail.credentials["password"] = config.getCredentials()
	mail.messageBuilder(mail.credentials["email"], mail.credentials["email"], mail.body)
	mail.sendMail()
	return

if __name__ == '__main__':
	sys.exit(main())



	

