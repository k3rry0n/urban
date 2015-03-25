#!/usr/bin/python3
import sys, urban, re

print("Starting session...")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		input_string = sys.argv[1]
		
		if re.findall('([а-яА-ЯёЁ])', input_string):
			print("Vodka, perestroika, Gorbachov")
			print("\nRussian is not allowed, now exiting...")
			exit()
    	
		a = urban.Urban(input_string)
		
		meanings = a.get_meanings() 
					
		if meanings is False:
			print("Nothing was found")
			exit()

		meanings, examples = meanings
		print(" ")
		print("\033[5mMeaning I found for {}\033[25m\n".format(input_string))
		num = 0
		for i, meaning in enumerate(meanings):
			num += 1
			print("{}. {}".format(num, meaning))
			print("EXAMPLE: " + examples[i] + "\n")

	else:
		"Invalid parameters. Exiting."