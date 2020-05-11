import speech_recognition as sr
from time import ctime
import webbrowser as wb
import playsound
import os
import random
import sys
import cv2
#import pyaudio
from gtts import gTTS
import time
r=sr.Recognizer()
r.energy_threshold=4000


n_folder='E://'

def record_audio(ask=False): 
    with sr.Microphone() as source:
        if ask:
            you_speak(ask)
        audio=r.listen(source)
        voice_data=''
        try:
            voice_data=r.recognize_google(audio)
        except sr.UnknownValueError:
            you_speak('sorry')
        except sr.RequestError:
            you_speak(' i am sorry')
        #return voice_data
        if voice_data=='exit':
            sys.exit().sys.exit()
        return voice_data

    
def you_speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,1000000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
    
            
def respond(voice_data):
    if 'what is your name' in voice_data:
        you_speak('My name is divya')
    elif 'time' in voice_data:
        you_speak(ctime())
    elif 'search' in voice_data:
        search=record_audio('What do you want for')
        url='https://google.com/search?q=' + search
        wb.get().open(url)
        you_speak('Here is what I found for '+ search)
    elif 'location' in voice_data:
        location=record_audio('Which location')
        url='https://www.google.nl/maps/place/' + location+'/&mp;'
        wb.get().open(url)
        you_speak('Here is the location '+ location)
    elif 'file' in voice_data:
        l=record_audio('which file')
        #open('E://')
        os.startfile("E://"+l)
        you_speak('open')
    elif 'new folder' in voice_data:
        j=record_audio("In which drive you want to create d or e")
        if j=='d':
            os.chdir ('D:\\')
            k=record_audio("What your new folder name")
            os.mkdir(k)
        elif j=='e':
            os.chdir ('E:\\')
            k=record_audio("What your new folder name")
            os.mkdir(k)
        you_speak('Your folder is added ') 
    elif 'open' in voice_data:
        l=record_audio("Which You Want to Open")
        l=l.upper()
        if l=='command prompt':
            os.system('cmd')
        elif l=='calculator':
            os.chdir(n_folder)
            os.system('calc')
        
           
time.sleep(2)
you_speak('How can I help you?')
while(True):
    voice_data=record_audio()
    #print(voice_data)
    respond(voice_data)
    