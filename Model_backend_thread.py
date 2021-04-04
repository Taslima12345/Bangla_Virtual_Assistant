import threading
import ctypes
import speech_recognition as sr
from google_trans_new import google_translator
from gtts import gTTS
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import easygui 
import autopy
import pyautogui
import pywhatkit
import random
from playsound import playsound
from os import path
import wave
import librosa
import webbrowser
import numpy as np
import tensorflow as tf


class VoiceCommandsListener(threading.Thread):


	def __init__(self, appUI=None):
		threading.Thread.__init__(self)

		self.uiController = appUI
		self._keep_running = True
		self.increase_command = "nircmd.exe changesysvolume 1000"
		self.decrease_command = "nircmd.exe changesysvolume -1000"
		self.voice_command_model = tf.keras.models.load_model(path.join (path.dirname(path.abspath(__file__)),'Model', 'VoiceCommandsModel.h5'))
		self.myAppPath = os.path.join(os.environ['USERPROFILE'], 'Bangla Virtual Assistant')
		if not os.path.exists(self.myAppPath):
			os.mkdir(self.myAppPath)
		
		self.audioFilePath = os.path.join(self.myAppPath, 'Audios')
		if not os.path.exists(self.audioFilePath):
			os.mkdir(self.audioFilePath)

		self.screenshotFilePath = os.path.join(self.myAppPath, 'Screenshot')
		if not os.path.exists(self.screenshotFilePath):
			os.mkdir(self.screenshotFilePath)
	
	def run(self):
		self.startListening()
			
	def terminate(self):
		self._keep_running = False
		# print("- Backend Listener has Stopped -")	
		
	def get_id(self):
		# returns id of the respective thread
		if hasattr(self, '_thread_id'):
			return self._thread_id
		for id, thread in threading._active.items():
			if thread is self:
				return id
				
	def raise_exception(self):
		thread_id = self.get_id()
		res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
		if res > 1:
			ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
			# print('Exception raise failure')
	
	def translate_To_Bangla(self,englis_text):
		translator = google_translator()
		bangla_text = translator.translate(englis_text, lang_src='en', lang_tgt='bn')   
		self.convert_to_aduio(bangla_text)

	def play_audio(self,path_of_audio):
		playsound(path_of_audio)

	def convert_to_aduio(self,translate_text):
		language = 'bn'
		myobj = gTTS(text=translate_text, lang=language, slow=False)
		myobj.save("voice.mp3") 
		self.play_audio('voice.mp3')

		os.remove('voice.mp3')

	def wishMe(self):
		hour=datetime.datetime.now().hour
		if hour>=0 and hour<12:
			speak1 = "Good Morning"
			self.translate_To_Bangla(speak1)
		
		elif hour>=12 and hour<18:		
			speak2 = "Good Afternoon"
			self.translate_To_Bangla(speak2)
			
		else:
			speak3 = "Good evening"
			self.translate_To_Bangla(speak3)

	def takeCommand(self):
		r = sr.Recognizer()
		with sr.Microphone() as source:
			print("Listening...")
			audio = r.listen(source)
			try:
				audio_path = path.join(path.dirname(path.abspath(__file__)), 'temp_audio.wav')
				with open(audio_path, 'wb') as fl:
					fl.write(audio.get_wav_data())
					# print("Audio file written")
				data, sampling_rate = librosa.load(path.join(path.dirname(path.abspath(__file__)), audio_path))
				D = np.abs(librosa.stft(data))
				temp = None
				temp = np.zeros((1025, 203))
				temp[: D.shape[0], : D.shape[1]] = D
				
				temp = temp.reshape((1, 1025, 203, 1))
				output_prediction = self.voice_command_model.predict(temp)
				# print(output_prediction)

				class_pred = np.argmax(output_prediction)
				confidence = max(output_prediction[0])

				print("class: ", class_pred)
				print("class confidence: ", confidence)				
				os.remove(path.join(path.dirname(path.abspath(__file__)), audio_path))
				return(class_pred, confidence)
			except Exception as err:
				speak4 = "আপনার কি আমার জন্য কোন নির্দেশনা রয়েছে? "
				self.translate_To_Bangla(speak4)
				return(-1, 0)

			
	def startListening(self):

		time.sleep(3)
		self.wishMe()

		while True:			
			statement, confidence = self.takeCommand()
			
			if  statement==0 and confidence>= 0.9 :
				self.uiController.show_input_command.setText("ওপেন উইকিপিডিয়া")
				speak210 = ("আপনি কি জানতে চান?")
				self.convert_to_aduio(speak210)
				query = self.takeCommand()
				self.uiController.output_present.setText(query)
				results = wikipedia.summary(query, sentences=3)
				self.uiController.output_present.setText(results)

			elif statement==2 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ওপেন ইউটিউব")
				webbrowser.open_new_tab("https://www.youtube.com")
				speak10 = "ইউটিউব চালু করা হয়েছে"
				self.convert_to_aduio(speak10)
				self.uiController.output_present.setText("ইউটিউব চালু করা হয়েছে")

			elif statement==1 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ওপেন গুগল")
				webbrowser.open_new_tab("https://www.google.com")
				speak11= "গুগল চালু করা হয়েছে"
				self.convert_to_aduio(speak11)				
				self.uiController.output_present.setText("গুগল চালু করা হয়েছে")

			elif statement==3 and confidence>= 0.9: 
				self.uiController.show_input_command.setText("ওপেন ফাইল এক্সপ্লোরার")
				fileopen = easygui.fileopenbox() 
				self.convert_to_aduio("ফাইল এক্সপ্লোরার চালু হয়েছে")
				self.uiController.output_present.setText("ফাইল এক্সপ্লোরার চালু হয়েছে")
			
			elif statement==7 and confidence>= 0.9:
				self.uiController.show_input_command.setText("স্ক্রিনশট নেওয়া")
				now = datetime.datetime.now()
				timenow = now.strftime("%H_%M_%S")
				filePath = path.join (self.screenshotFilePath, str(datetime.date.today()))
				fileName = timenow+'.png'
				myss = pyautogui.screenshot()
				try:
					myss.save(path.join(filePath, fileName))
				except FileNotFoundError:
					os.mkdir(filePath)
					myss.save(path.join(filePath,fileName))     
				
				self.convert_to_aduio("স্ক্রিনশট নেওয়া হয়েছে")
				self.uiController.showScreenshotImage(path.join(filePath, fileName))			
				
			elif statement==11 and confidence>= 0.9:
				
				self.uiController.show_input_command.setText("আবহাওয়ার আপডেট")
				api_key="8ef61edcf1c576d65d836254e11ea420"
				base_url="https://api.openweathermap.org/data/2.5/weather?"
				# speak10 = ("What's the Place name")
				self.translate_To_Bangla("জায়গার নাম বলুন")
				city_name= self.takeCommand()
				complete_url=base_url+"appid="+api_key+"&q="+city_name
				response = requests.get(complete_url)
				x=response.json()
				if x["cod"]!="404":
					y=x["main"]
					current_temperature = y["temp"]
					current_humidiy = y["humidity"]
					z = x["weather"]
					weather_description = z[0]["description"]
					details_weather = (" Temperature in kelvin unit : " +  str(current_temperature) + "\nAnd humidity : " + str(current_humidiy) + " percentage")
					translator = google_translator()
					bangla_text_weather = translator.translate(details_weather, lang_src='en', lang_tgt='bn') 

					self.uiController.output_present.setText(bangla_text_weather)
					self.convert_to_aduio(bangla_text_weather)				
				else:
					speak14 = (" দুঃখিত, খুঁজে পাই নি। দয়া করে আবার বলুন ")
					self.convert_to_aduio(speak11)				

			elif statement==8 and confidence>= 0.9:
				
				self.uiController.show_input_command.setText("সময়")
				dayDate = datetime.datetime.now().strftime("%a, %b %d, %Y")
				speak_date2 =f"{dayDate}"			
				currTime = datetime.datetime.now().strftime("%I:%M:%S %p")
				speak_time = f"{currTime}" 
				
				total_output = ("Today " + speak_date2 + "\nand time  " + speak_time)
				translator = google_translator()
				bangla_text_time = translator.translate(total_output, lang_src='en', lang_tgt='bn')
				self.uiController.output_present.setText(bangla_text_time)
				self.convert_to_aduio(bangla_text_time)

			elif statement==5 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ল্যাপটপ শাটডাওন")
				speak19 = ("ঠিক আছে, আপনার পিসি 10 সেকেন্ডের মধ্যে বন্ধ হয়ে যাবে,নিশ্চিত করে নিন যে আপনি সমস্ত অ্যাপ্লিকেশন বন্ধ করেছেন")
				self.uiController.output_present.setText(speak19)
				# self.translate_To_Bangla(speak19)
				subprocess.call(["shutdown", "/s"])
				# self.uiController.output_present.setText("")

			elif statement==4 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ল্যাপটপ রিস্টার্ট")
				speak20 = ("ঠিক আছে, আপনার পিসি 10 সেকেন্ডের মধ্যে রিস্টার্ট নিবে,নিশ্চিত করে নিন যে আপনি সমস্ত অ্যাপ্লিকেশন বন্ধ করেছেন")
				self.uiController.output_present.setText("ঠিক আছে, আপনার পিসি 10 সেকেন্ডের মধ্যে রিস্টার্ট নিবে,নিশ্চিত করে নিন যে আপনি সমস্ত অ্যাপ্লিকেশন বন্ধ করেছেন")
				os.system("shutdown /r")
				
			elif statement==6 and confidence>= 0.9:
				self.uiController.show_input_command.setText("গান প্লে করা")
				music_dir = "C:\\Users\\S\\Music"
				songs = os.listdir(music_dir)
				rd = random.choice(songs)
				os.startfile(os.path.join(music_dir, rd))
				self.uiController.output_present.setText("গান প্লে করা হয়েছে")
				
			elif statement==9 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ভলিউম বাড়ানো")	
				subprocess.run(self.increase_command, shell=True)
				self.uiController.output_present.setText("ভলিউম বাড়ানো হয়েছে")
			
			elif statement==10 and confidence>= 0.9:
				self.uiController.show_input_command.setText("ভলিউম কমানো")
				subprocess.run(self.decrease_command, shell=True)
				self.uiController.output_present.setText("ভলিউম কমানো হয়েছে")

if __name__ == "__main__":
	try:		
		self = None
		obj = VoiceCommandListener(self)
		obj.start()
	except Exception as err:
		print("ERROR in hashtag fetching: ", err)
		

	
		
		