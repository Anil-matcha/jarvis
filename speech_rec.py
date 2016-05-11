import subprocess
import os
import speech_recognition as sr
import time
r = sr.Recognizer()
m = sr.Microphone()

fav_song_path = "path to song"

def execute_command(string):
    if("play" in string):
        subprocess.Popen(['path to espeak.exe', "Playing your favorite song sir"])
        time.sleep(2)
        subprocess.Popen([r'path to vlc.exe', fav_song_path])
def listen_to_audio():
	try:
		print("A moment of silence, please...")
		with m as source: r.adjust_for_ambient_noise(source)
		print("Set minimum energy threshold to {}".format(r.energy_threshold))
		print("Say something!")
		with m as source: audio = r.listen(source)
		print("Got it! Now to recognize it...")
		try:
			# recognize speech using Google Speech Recognition
			value = r.recognize_google(audio)

			# we need some special handling here to correctly print unicode characters to standard output
			if str is bytes: # this version of Python uses bytes for strings (Python 2)
				print(u"You said {}".format(value).encode("utf-8"))
				execute_command(u"{}".format(value).encode("utf-8"))
			else: # this version of Python uses unicode for strings (Python 3+)
				print("You said {}".format(value))
				execute_command("{}".format(value))
		except sr.UnknownValueError:
			print("Oops! Didn't catch that")
		except sr.RequestError as e:
			print("Uh oh! Couldn't request results from Google Speech Recognition service; {0}".format(e))
	except KeyboardInterrupt:
		pass
	
		
while(True):
    listen_to_audio()
    time.sleep(1)
