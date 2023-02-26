import json
import random

class syntax:
	def __init__(self):
		self.codes = json.loads(open("data/codes.json", "r").read())['codes']
	
	def getCode(self):
		n = random.randint(0, len(self.codes) - 1)
		code = self.codes[n]
		return code
	
	def setSecretCode(self, code):
		splits = code.split("____")
		result = ""

		for i in range(len(splits)):
			if splits[0] != "" and i == 0:
				result += f"{splits[i]}"
			elif i != 0:
				result += f"{i}. ____ {splits[i]}"
		
		return result
	
	def checkCode(self, code):
		exec(code)
		