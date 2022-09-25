import os
import pyttsx3
import math
voice = pyttsx3.init()
voice.setProperty('rate', 145) # Just put it a little slow for proper understanding

while True:
	quote = input("Enter something to say: ")
	if quote.startswith("*cal"): # This is where the "*cal" special command is detected
		words = quote.split("*cal", 1) # The user string is split into two parts
		answer = eval(words[1]) # It processes and calculates the second part
		print(answer)
		voice.say(answer)
	else:
		voice.say(quote)
	voice.runAndWait()
	if(os.name == "nt"):
		os.system("cls")
	elif(os.name == "posix"):
		os.system("clear")