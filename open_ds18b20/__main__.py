import sys
import file, mail, probe

config = file.ConfigFile("./config.json")
files = []
probes = probe.Probe()



def main():
	probes.detectProbe()
	for p in range(len(probes.listprobes)):
		files.append(file.ProbeFile(listprobes))
		templine = files[p].readline(2)
		probes.getTemperatures(templine)
	email = mail.Mail()
	email.messageBody(probes.temperatures)
	email.credentials["email"], email.credentials["password"] = config.getCredentials()
	email.messageBuilder(email.credentials["email"], email.credentials["email"], email.body)
	email.sendMail()
	return

if __name__ == '__main__':
	sys.exit(main())



	

