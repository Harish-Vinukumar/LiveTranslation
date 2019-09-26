# import necessary libraries
import speech_recognition as sr  
from gtts import gTTS, lang
import os
from googletrans import Translator
from pygame import mixer

#getting source and destination languages
print("Languages Available for Translation:")
lang_dict = lang.tts_langs()
lang_name = list(lang_dict.values())
size = len(lang_dict)
lang_format = list(lang_dict.keys())
for i in range(size):
    print(i,': ',lang_name[i])

src = input("Enter the source language: ")
dest = input("Enter the destinatin language: ")
s = 0
d = 0

try:
    s = int(src)
    d = int(dest)
except ValueError:
    print("Please provide the respective index value!!")

source = ''
destination = ''

if s >= size and d >= size:
    print("Please provide the input from the given set of languages!!")
else:
    source = lang_format[s]
    destination = lang_format[d]

			
# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as srcs:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(srcs)   
text = ''
try:
    text = r.recognize_google(audio, language=source)
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))

#translate to the destination language
translator = Translator()
result = translator.translate(text, dest=destination).text

#save it in a audio file
audio=gTTS(text=result,lang=destination,slow=False)
audio.save("sample.mp3")

#play the audio file
mixer.init()
mixer.music.load("sample.mp3")
mixer.music.play()





