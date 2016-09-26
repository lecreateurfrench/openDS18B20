#!/usr/bin/python
from opend18b20 import file
import re
import os

class Probe():

	def __init__(self):
		self.probes = {}
		self.temperatures = {}
		self.path = os.path.abspath("/sys/bus/w1/devices")
		return


	def getTemperature(self, line, i):
		regexp = r"^\d+$"
		temp = re.match(regexp, line).groups[0]
		temp = list(temp)
		self.temperatures.append(temp[0]+temp[1]+","+temp[2]+"C")
			#self.temperatures[key] = file.readline(probes[key].as_string() + "/w1_slave")

		return

	def detectProbe(self):
		regexp = r"^28"
		num = 0
		for directory in os.listdir(path):
			if re.match(regexp, directory):
				self.probes["probe " + num.as_string()] = directory
				self.temperatures["probe " + num.as_string()] = ""
				num += 1
		return probes
