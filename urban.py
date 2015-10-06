#!/usr/bin/python3
import requests, re
import logging

class Urban(object):

	def __init__(self, word):
		self.meanings = []
		self.examples = []
		self.word = word

	def get_meanings(self):
		
		self.find_meaning(self.word)
		return self.meanings, self.examples

	def find_meaning(self, input_string):
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

		ex = 0
		
		try:
			for i in meanings:

				self.meanings.append("{}".format(i.replace("\n", "").replace("&#39;", "'").replace("&quot;", '"').replace("\r", "")))
				self.examples.append("{}".format(examples[ex].replace("\n", "").replace("&#39;", "'").replace("&quot;", '"').replace("\r", "")))
				ex += 1
		except:
			print("No Meanings found. Now exiting...")
			exit()