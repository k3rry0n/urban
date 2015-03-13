#!/usr/bin/python3
import requests, sys, re

def print_inversion(text_to_print):
	return "{}{}{}".format("\033[7m", text_to_print, "\033[27m")

def print_bold(text_to_print):	
	return "{}{}{}".format("\033[1m", text_to_print, "\033[22m")

def find_meaning(input_string):
	http = requests.session()
	url = "http://urbandictionary.com"
	page = http.get(url)
	
	# парсим токен
	parsed_list = re.findall('authenticity_token\"\ type=\"hidden\" value=\"([^"]+)', page.text)

	if not parsed_list:
		print("Nothing was found :(")

	data = {
		'authenticity_token': parsed_list[0],
		'term': input_string
		}

	print("Sending info to urbandictionary...")

	search_result = http.post("http://www.urbandictionary.com/search.php", data)

	meanings = re.findall("<div class='meaning'>([^<]+)", search_result.text)
	examples = re.findall("class='example'>([^<]+)", search_result.text)

	print(print_inversion(input_string))
	print(print_bold("Meaning I found: "))
	
	ex = 0
	
	for i in meanings:
		print("==========\n")
		print(print_bold("{}. {}".format(ex, i.replace("\n", "").replace("&#39;", "'").replace("&quot;", '"'))))
		print(print_inversion("{}".format(examples[ex].replace("\n", "").replace("&#39;", "'").replace("&quot;", '"'))))
		ex += 1

print("\n")
print("Starting session...")
print("\n")

if __name__ == "__main__":
	if len(sys.argv) == 2:
		input_string = sys.argv[1]
		
		if re.findall('([а-яА-ЯёЁ])', input_string):
			print("Vodka, perestroika, Gorbachov")
			print("\nRussian is not allowed, now exiting...")
			exit()
    	
		find_meaning(input_string)
	else:
		"Invalid parameters. Exiting."