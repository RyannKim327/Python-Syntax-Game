from utils.secret import syntax

if __name__ == "__main__":
	syn = syntax()
	code = syn.getCode()
	print(syn.setSecretCode(code))

	compiled = ""

	splits = code.split("____")
	for i in range(1, len(splits)):
		c = input(f"{i}. ")
		compiled += c + splits[i]
	
	syn.checkCode(compiled)