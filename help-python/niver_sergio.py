def willDanielShowThis(isDanielCool):
	if isDanielCool == True:
		return True
	return False

def main():
	isSergiosBirthday = True
	i = 0
	while(i < 6):
		if(willDanielShowThis(isSergiosBirthday)):
			print("Feliz Aniversário, Sérgio")
		i += 1

if __name__ == "__main__":
	main()
