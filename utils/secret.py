import json
import random

class syntax:
	def __init__(self):
		self.codes = json.loads(open("data/codes.json", "r").read())['codes']
	
	def getCode(self):
		n = random.randint(0, len(self.code) - 1)
		return self.codes