#!/usr/bin/python3
import os, subprocess, urban
# cunt
n = subprocess.Popen("xsel -o", shell=True, stdout=subprocess.PIPE)

string, status = n.communicate()
a = urban.Urban(string)
meanings = a.get_meanings() 
meanings, examples = meanings
result = "{}\n============\nEXAMPLE: {}".format(meanings[0], examples[0]).replace("'", "")
os.system("notify-send '<b>{}</b>' '{}'".format(string.decode(), result))
