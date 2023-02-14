# -*- coding: utf-8 -*-

import re
import openai
import speech_recognition as sr
import pyttsx3
#import winsound

from deep_translator import GoogleTranslator

# language
LANG = 'en' # en -> english, pt-> portuguese

# init the AI
print('Init AI')
openai.api_key = 'PUT-YOR-API-KEY-HERE' # <- OpenAi API key (openai.com/api)
model_engine = 'text-davinci-003'

# params
temperature = 0.5
max_tokens=1024

# init the recognizer
print('Init recognizer')
req = sr.Recognizer()

# voice engine
engine = pyttsx3.init()

# text to speak routine
def SpeakText(command):
	print('Text to speak...')
	#engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
# some utils
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""	
	
# loop infinitely for user to speak
print('Init speech to text')
while(1):
	try:
		with sr.Microphone() as source2:
			print('Waiting...')
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			req.adjust_for_ambient_noise(source2, duration = 1.0)
			
			print('Listening... (Ex: Computer, how are you doing?')
			# listens for the urser's input
			audio2 = req.listen(source2)			
			
			print('Recognizing...')
			# using google to recognize audio
			MyText = req.recognize_google(audio2, language=LANG)
			MyText = MyText.lower()
			
			if (('Computer' in MyText) or ('computer' in MyText.lower())):
				# beep
				#winsound.Beep(415, 250)
				
				MyText = MyText.replace('Computer', '').replace('computer', '')
				
				# Translating
				MyText = GoogleTranslator(source='auto', target=LANG).translate(MyText)			
				
				# beep
				#winsound.Beep(523, 250)
			
				# AI
				print('Thinking...')
				completion = openai.Completion.create(
					engine=model_engine, 
					prompt=MyText, 
					max_tokens=max_tokens, 
					n = 1, 
					stop = None, 
					temperature = temperature,
					top_p=0.3,
					frequency_penalty=0.5,
					presence_penalty=0.0
					)
				MyMessage = completion.choices[0].text
				
				
				print("User: {}".format(MyText))
				print("Computer: {}".format(MyMessage))
				SpeakText(MyMessage)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	except sr.UnknownValueError:
		# print("Unknown error ocurred.") # unknown error
		print("") # print nothing
