# import speech_recognition as sr
# import pint

# r = sr.Recognizer()
# with sr.Microphone() as source:
# 	print "say"                # use the default microphone as the audio source
# 	audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
# 	print r.recognize(audio)   # recognize speech using Google Speech Recognition
# # except LookupError:                            # speech is unintelligible
# #     print("Could not understand audio")
import speech_recognition as s
import pyttsx  
import os 
def du(user_input):
	user_input2='"'+user_input+'"'
	user_input2=user_input2.lower()
	print user_input2
	
	os.system(user_input2)
	if "calculator" in user_input:
		os.system("gnome-calculator")
	if "sublime" in user_input:
		os.system("subl")
choice=input("enter your choice:\n1.voice 2.keyboard")
count=1
while choice==1:
	speech_engine = pyttsx.init() # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
	speech_engine.setProperty('rate', 150)
	# choice=input("enter your choice:\n1.voice 2.keyboard")
	


	def speak(text):
		speech_engine.say(text)
		speech_engine.runAndWait()

	recognizer = s.Recognizer()

	def listen():
		with s.Microphone() as source:
			recognizer.adjust_for_ambient_noise(source)
			audio = recognizer.listen(source)
			aig=recognizer.recognize_google(audio)
			return aig
			print aig
	if count==1:
		speak("I am jarvis at your service")
	else:
		speak("ASK")
	
	# speak(listen())		

	user_input=listen()
	if user_input:
		du(user_input)
		print user_input
		count+=1	
while choice==2:	
	user_input1=raw_input("enter")
	if user_input1:
		user_input=user_input1
		du(user_input)
		print user_input
