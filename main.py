from __future__ import unicode_literals
import speech_recognition as sr
import pyttsx3
import os
import os.path
import re
import webbrowser
import requests
import sys
import datetime
import wikipedia
import youtube_dl
import urllib.request
import urllib.parse
import ffmpeg
import pygame
from pyowm import OWM
from googleapiclient.discovery import build
from playsound import playsound
from threading import Thread
from time import sleep

engine = pyttsx3.init()
today = datetime.date.today()
t = datetime.datetime.now()
api_key = '****************************'
youtube = build('youtube', 'v3', developerKey=api_key)
(width, height) = (100, 100)
pygame.mixer.init()
volume = 0.5

#Wake Word
f = open("wakeWord.txt", "r")
wakeWord = f.read()
f.close()

def playPlaylist(playlist):
    mixer.init()
    for music in playlist:
        mixer.music.load(music)
        mixer.music.play()
        while mixer.music.get_busy():
            sleep(1)

def myCommand():
    #Listen for the command
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready for your command...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('you said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):

    global wakeWord
    global youtube
    global volume
    
    #if statements for executing commands

    #change 'computer' to wakeWord
    if wakeWord in command:

        pygame.mixer.music.set_volume(0.1)
        playsound('sounds/wakeSound.mp3')
        actualCommand = 0

        while actualCommand != 1:
            #sets the variable
            cmd = myCommand()
            
            #Opening a website
            if 'open the website' in cmd:
                reg_ex = re.search('open the website (.+)', cmd)
                if reg_ex:
                    domain = reg_ex.group(1)
                    url = 'http://www.' + domain
                    webbrowser.open(url)
                    pygame.mixer.music.set_volume(0.1)
                    engine.say('Opening website ' + domain + 'now')
                    engine.runAndWait()
                    
                actualCommand = 1

            #Opening a subreddit
            elif 'r /' in cmd:
                reg_ex = re.search('r / (.+)', cmd)
                if reg_ex:
                    subreddit = reg_ex.group(1)
                    subreddit = re.sub(' ', '', subreddit)
                    subredditurl = 'https://www.reddit.com/r/' + subreddit
                    webbrowser.open(subredditurl)

                    pygame.mixer.music.set_volume(0.1)
                    engine.say('Opening R / ' + subreddit + ' now')
                    engine.runAndWait()
                    
                actualCommand = 1

            #Opening a subreddit
            elif 'r/' in cmd:
                reg_ex = re.search('r/(.+)', cmd)
                if reg_ex:
                    subreddit = reg_ex.group(1)
                    subreddit = re.sub(' ', '', subreddit)
                    subredditurl = 'https://www.reddit.com/r/' + subreddit
                    webbrowser.open(subredditurl)

                    pygame.mixer.music.set_volume(0.1)
                    engine.say('Opening R / ' + subreddit + ' now')
                    engine.runAndWait()
                    
                actualCommand = 1

            #Opening Youtube
            elif 'search youtube for' in cmd:
                reg_ex = re.search('search youtube for (.+)', cmd)
                if reg_ex:
                    youtubeSearch = reg_ex.group(1)
                    youtubeSearchURL = 'https://www.youtube.com/results?search_query=' + youtubeSearch
                    webbrowser.open(youtubeSearchURL)

                pygame.mixer.music.set_volume(0.1)
                engine.say('Searching youtube for ' + youtubeSearch + 'now')
                engine.runAndWait()
                
                actualCommand = 1

            #Searching on Youtube
            elif 'open youtube' in cmd:
                youtube = 'https://youtube.com'
                webbrowser.open(youtube)

                pygame.mixer.music.set_volume(0.1)
                engine.say('Opening YouTube now')
                engine.runAndWait()
                
                actualCommand = 1

            #Tell the time
            elif 'what time is it' in cmd:
                pygame.mixer.music.set_volume(0.1)
                engine.say('It is currently')
                engine.say(datetime.datetime.now().hour)
                engine.say(datetime.datetime.now().minute)
                engine.runAndWait()
                
                actualCommand = 1

            #Tells the date
            elif 'what day is it' in cmd:
                pygame.mixer.music.set_volume(0.1)
                engine.say('It is')
                engine.say(datetime.date.today())
                engine.runAndWait()
                
                actualCommand = 1

            #Volume
            elif 'volume' in cmd:
                if '10' in cmd:
                    volume = 1
                    pygame.mixer.music.set_volume(1)
                    engine.setProperty('volume', 1)
                    engine.say('Volume set to 10')
                    engine.runAndWait()
                    actualCommand = 1

                elif '2' in cmd:
                    volume = 0.2
                    pygame.mixer.music.set_volume(0.2)
                    engine.setProperty('volume', 0.2)
                    engine.say('Volume set to 2')
                    engine.runAndWait()
                    actualCommand = 1

                elif '3' in cmd:
                    volume = 0.3
                    pygame.mixer.music.set_volume(0.3)
                    engine.setProperty('volume', 0.3)
                    engine.say('Volume set to 3')
                    engine.runAndWait()
                    actualCommand = 1

                elif '4' in cmd:
                    volume = 0.4
                    pygame.mixer.music.set_volume(0.4)
                    engine.setProperty('volume', 0.4)
                    engine.say('Volume set to 4')
                    engine.runAndWait()
                    actualCommand = 1

                elif '5' in cmd:
                    volume = 0.5
                    pygame.mixer.music.set_volume(0.5)
                    engine.setProperty('volume', 0.5)
                    engine.say('Volume set to 5')
                    engine.runAndWait()
                    actualCommand = 1

                elif '6' in cmd:
                    volume = 0.6
                    pygame.mixer.music.set_volume(0.6)
                    engine.setProperty('volume', 0.6)
                    engine.say('Volume set to 6')
                    engine.runAndWait()
                    actualCommand = 1

                elif '7' in cmd:
                    volume = 0.7
                    pygame.mixer.music.set_volume(0.7)
                    engine.setProperty('volume', 0.7)
                    engine.say('Volume set to 7')
                    engine.runAndWait()
                    actualCommand = 1

                elif '8' in cmd:
                    volume = 0.8
                    pygame.mixer.music.set_volume(0.8)
                    engine.setProperty('volume', 0.8)
                    engine.say('Volume set to 8')
                    engine.runAndWait()
                    actualCommand = 1

                elif '9' in cmd:
                    volume = 0.9
                    pygame.mixer.music.set_volume(0.9)
                    engine.setProperty('volume', 0.9)
                    engine.say('Volume set to 9')
                    engine.runAndWait()
                    actualCommand = 1

                elif '1' in cmd:
                    volume = 0.1
                    pygame.mixer.music.set_volume(0.1)
                    engine.setProperty('volume', 0.1)
                    engine.say('Volume set to 1')
                    engine.runAndWait()
                    actualCommand = 1

                elif '0' in cmd:
                    volume = 0
                    pygame.mixer.music.set_volume(0)
                    engine.setProperty('volume', 0)
                    engine.say('Volume set to 0')
                    engine.runAndWait()
                    actualCommand = 1
                
                elif 'ten' in cmd:
                    volume = 1
                    pygame.mixer.music.set_volume(1)
                    engine.setProperty('volume', 1)
                    engine.say('Volume set to 10')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'two' in cmd:
                    volume = 0.2
                    pygame.mixer.music.set_volume(0.2)
                    engine.setProperty('volume', 0.2)
                    engine.say('Volume set to 2')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'three' in cmd:
                    volume = 0.3
                    pygame.mixer.music.set_volume(0.3)
                    engine.setProperty('volume', 0.3)
                    engine.say('Volume set to 3')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'four' in cmd:
                    volume = 0.4
                    pygame.mixer.music.set_volume(0.4)
                    engine.setProperty('volume', 0.4)
                    engine.say('Volume set to 4')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'five' in cmd:
                    volume = 0.5
                    pygame.mixer.music.set_volume(0.5)
                    engine.setProperty('volume', 0.5)
                    engine.say('Volume set to 5')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'six' in cmd:
                    volume = 0.6
                    pygame.mixer.music.set_volume(0.6)
                    engine.setProperty('volume', 0.6)
                    engine.say('Volume set to 6')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'seven' in cmd:
                    volume = 0.7
                    pygame.mixer.music.set_volume(0.7)
                    engine.setProperty('volume', 0.7)
                    engine.say('Volume set to 7')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'eight' in cmd:
                    volume = 0.8
                    pygame.mixer.music.set_volume(0.8)
                    engine.setProperty('volume', 0.8)
                    engine.say('Volume set to 8')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'nine' in cmd:
                    volume = 0.9
                    pygame.mixer.music.set_volume(0.9)
                    engine.setProperty('volume', 0.9)
                    engine.say('Volume set to 9')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'one' in cmd:
                    volume = 0.1
                    pygame.mixer.music.set_volume(0.1)
                    engine.setProperty('volume', 0.1)
                    engine.say('Volume set to 1')
                    engine.runAndWait()
                    actualCommand = 1

                elif 'zero' in cmd:
                    volume = 0
                    pygame.mixer.music.set_volume(0)
                    engine.setProperty('volume', 0)
                    engine.say('Volume set to 0')
                    engine.runAndWait()
                    actualCommand = 1

            #Mute
            elif 'mute' in cmd:
                pygame.mixer.music.set_volume(0)
                engine.setProperty('volume', 0)
                engine.say('muted')
                engine.runAndWait()
                actualCommand = 1

            #Unmute
            elif 'unmute' in cmd:

                pygame.mixer.music.set_volume(volume)
                engine.setProperty('volume', volume)
                engine.say('Unmuted')
                engine.runAndWait()
                actualCommand = 1

            #Tells a joke
            elif 'tell me a joke' in cmd:
                res = requests.get(
                        'https://icanhazdadjoke.com/',
                        headers={"Accept":"application/json"}
                        )
                if res.status_code == requests.codes.ok:
                    pygame.mixer.music.set_volume(0.1)
                    engine.say(str(res.json()['joke']))
                    engine.runAndWait()
                    
                else:
                    pygame.mixer.music.set_volume(0.1)
                    engine.say('oops!I ran out of jokes')
                    engine.runAndWait()
                    
                actualCommand = 1

            #Tells a joke
            elif 'tell me another joke' in cmd:
                res = requests.get(
                        'https://icanhazdadjoke.com/',
                        headers={"Accept":"application/json"}
                        )
                if res.status_code == requests.codes.ok:
                    pygame.mixer.music.set_volume(0.1)
                    engine.say(str(res.json()['joke']))
                    engine.runAndWait()
                    
                else:
                    pygame.mixer.music.set_volume(0.1)
                    engine.say('oops!I ran out of jokes')
                    engine.runAndWait()
                    
                actualCommand = 1

            #Wikipedia
            elif 'tell me about' in cmd:
                reg_ex = re.search('tell me about (.*)', cmd)
                try:
                    if reg_ex:
                        topic = reg_ex.group(1)
                        ny = wikipedia.page(topic)
                        pygame.mixer.music.set_volume(0.1)
                        engine.say(ny.content[:500].encode('utf-8'))
                        engine.runAndWait()
                        

                except Exception as e:
                    pygame.mixer.music.set_volume(0.1)
                    engine.say(e)
                    engine.runAndWait()
                    
                actualCommand = 1

            #Weather
                #BUG - API key
            elif 'current weather' in cmd:
                reg_ex = re.search('current weather in (.*)', cmd)
                if reg_ex:
                    city = reg_ex.group(1)
                    owm = OWM(API_key='*************************')
                    obs = owm.weather_at_place(city)
                    w = obs.get_weather()
                    k = w.get_status()
                    x = w.get_temperature(unit='celsius')
                    pygame.mixer.music.set_volume(0.1)
                    engine.say('Current weather in %s is %s. The current temperature is %0.1f degree celcius. The maximum temperature is %0.1f degree celcius and the minimum temperature is %0.1f degree celcius' % (city, k, x['temp'], x['temp_max'], x['temp_min']))
                    engine.runAndWait()
                    
                actualCommand = 1

            #Playlist
            elif 'playlist' in cmd:

                #create
                if 'create' in cmd:
                    engine.say('What would you like your playlist to be called?')
                    engine.runAndWait()
                    playlistNameConfirm = False
                    while playlistNameConfirm == False:
                        playlistName = myCommand()
                        engine.say('do you want your playlist to be called '+playlistName)
                        engine.runAndWait()
                        
                        pNameConfirm = myCommand()
                        if 'yes' in pNameConfirm:
                            playlistNameConfirm = True
                            engine.say('ok')
                            engine.runAndWait()
                        else:
                            engine.say('What do you want the playlist to be called?')
                            engine.runAndWait()
                    
                    engine.say('what song do you want to add?')
                    engine.runAndWait()
                    song = myCommand()
                    playlist = []
                    
                    request = youtube.search().list(
                        part='id',
                        maxResults=1,
                        q=song,
                        type='video',
                        fields='items/id'
                        )
                    response = request.execute()

                    ytID = response['items'][0]['id']['videoId']

                    alreadyGot = os.path.exists('music/'+ytID+'.mp3')

                    print (alreadyGot)

                    ##alreadyGot = str(alreadyGot)

                    if alreadyGot != True:
                        pygame.mixer.music.set_volume(0.1)
                        engine.say('you\'ve never played this song before so Ill just have to download it. This will take a few seconds')
                        engine.runAndWait()
                        url = "http://www.youtube.com/watch?v=" + ytID

                        ydl_opts = {
                            'format': 'bestaudio/best',
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                            }],
                            'outtmpl': '/music/%(id)s.%(ext)s',
                        }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])

                        addedSong = (song,'has been added to',playlist)
                        engine.say(addedSong)
                        engine.runAndWait()
                        playlist.append(ytID)

                    else:
                        addedSong = (song,'has been added to',playlist)
                        engine.say(addedSong)
                        engine.runAndWait()
                        playlist.append(ytID)
                            
                    add = False

                    while add == False:
                        engine.say('would you like to add another song?')
                        engine.runAndWait()
                        addSong = myCommand()
                        
                        if 'yes' in addSong:
                            engine.say('What song would you like me to add to '+ playlistName)
                            engine.runAndWait()
                            song = myCommand()
                            request = youtube.search().list(
                                part='id',
                                maxResults=1,
                                q=song,
                                type='video',
                                fields='items/id'
                                )
                            response = request.execute()

                            ytID = response['items'][0]['id']['videoId']

                            alreadyGot = os.path.exists('music/'+ytID+'.mp3')

                            print (alreadyGot)

                            ##alreadyGot = str(alreadyGot)

                            if alreadyGot != True:
                                pygame.mixer.music.set_volume(0.1)
                                engine.say('you\'ve never played this song before so Ill just have to download it. This will take a few seconds')
                                engine.runAndWait()
                                url = "http://www.youtube.com/watch?v=" + ytID

                                ydl_opts = {
                                    'format': 'bestaudio/best',
                                    'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                    }],
                                    'outtmpl': '/music/%(id)s.%(ext)s',
                                }
                                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                                    ydl.download([url])

                                addedSong = (song,'has been added to '+playlist)
                                engine.say(addedSong)
                                engine.runAndWait()
                                playlist.append(ytID)

                            else:
                                addedSong = (song,'has been added to '+playlist)
                                engine.say(addedSong)
                                engine.runAndWait()
                                playlist.append(ytID)
                        
                        else:
                            engine.say('ok')
                            engine.runAndWait()
                            pass
                            add = True

                        with open("playlists/"+playlistName+".txt", 'w') as filehandle:
                            for listitem in playlist:
                                filehandle.write('%s\n' % listitem)
                                
                    actualCommand = 1

                elif 'play' in cmd:

                    #play playlist
                    engine.say('which playlist would you like me to play?')
                    engine.runAndWait()
                    playingPlaylist = myCommand()

                    existing = os.path.exists('playlists/'+playingPlaylist+'.txt')

                    if existing == True:
                        engine.say('now playing'+playingPlaylist)
                        engine.runAndWait()

                        playlist = []
                        with open("playlists/"+playingPlaylist+".txt", 'r') as filehandle:
                            
                            playlist = [currentSong.rstrip() for currentSong in filehandle.readlines()]
                          
##                            for line in filehandle:
##                                currentSong = line[:-1]
##
##                                playlist.append(currentSong)

                        
##                        print(playlist)
##                        pygame.mixer.music.load('music/'+playlist.pop()+'.mp3')
##                        pygame.mixer.music.queue('music/'+playlist.pop()+'.mp3')
##                        pygame.mixer.music.set_endevent(pygame.USEREVENT)
##                        pygame.mixer.music.play()
##
##                        running = True
##                        while running:
##                           for event in pygame.event.get():
##                              if event.type == pygame.USEREVENT:    # A track has ended
##                                 if len ( playlist ) > 0:       # If there are more tracks in the queue...
##                                    pygame.mixer.music.queue ( playlist.pop() ) # Q
                        Thread(target=playPlaylist, args=(playlist,)).start()

                    else:
                        engine.say('That playlist doesnt exist')
                        engine.runAndWait()
                        

                    actualCommand = 1

            #add song to a playlist
            elif ('add' and 'song' and 'playlist') in cmd:
                engine.say('Which playlist would you like to add a song to?')
                engine.runAndWait()
                playlistAdd = myCommand()

                existing = os.path.exists('playlists/'+playingPlaylist+'.mp3')

                if existing == True:

                    f = open("playlists/"+playlistAdd+".txt", "r")
                    playlist = f.read()
                    f.close()

                    engine.say('what song do you want to add?')
                    engine.runAndWait()
                    song = myCommand()
                    
                    request = youtube.search().list(
                        part='id',
                        maxResults=1,
                        q=song,
                        type='video',
                        fields='items/id'
                        )
                    response = request.execute()

                    ytID = response['items'][0]['id']['videoId']

                    alreadyGot = os.path.exists('music/'+ytID+'.mp3')

                    print (alreadyGot)

                    ##alreadyGot = str(alreadyGot)

                    if alreadyGot != True:
                        pygame.mixer.music.set_volume(0.1)
                        engine.say('you\'ve never played this song before so Ill just have to download it. This will take a few seconds')
                        engine.runAndWait()
                        url = "http://www.youtube.com/watch?v=" + ytID

                        ydl_opts = {
                            'format': 'bestaudio/best',
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                            }],
                            'outtmpl': '/music/%(id)s.%(ext)s',
                        }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])

                        addedSong = (song,'has been added to',playlist)
                        engine.say(addedSong)
                        engine.runAndWait()
                        playlist.append(ytID)

                    else:
                        addedSong = (song,'has been added to',playlist)
                        engine.say(addedSong)
                        engine.runAndWait()
                        playlist.append(ytID)

                else:
                    engine.say('that playlist doesnt exist')
                    engine.runAndWait()
                        
                actualCommand = 1

            #Song
            elif 'play' in cmd:
                reg_ex = re.search('play (.*)', cmd)
                if reg_ex:
                    song = reg_ex.group(1)
                
                    request = youtube.search().list(
                        part='id',
                        maxResults=1,
                        q=song,
                        type='video',
                        fields='items/id'
                        )
                    response = request.execute()

                    ytID = response['items'][0]['id']['videoId']

                    alreadyGot = os.path.exists('music/'+ytID+'.mp3')

                    print (alreadyGot)

                    ##alreadyGot = str(alreadyGot)

                    if alreadyGot != True:
                        pygame.mixer.music.set_volume(0.1)
                        engine.say('you\'ve never played this song before so Ill just have to download it. This will take a few seconds')
                        engine.runAndWait()
                        url = "http://www.youtube.com/watch?v=" + ytID

                        ydl_opts = {
                            'format': 'bestaudio/best',
                            'postprocessors': [{
                                'key': 'FFmpegExtractAudio',
                                'preferredcodec': 'mp3',
                                'preferredquality': '192',
                            }],
                            'outtmpl': '/music/%(id)s.%(ext)s',
                        }
                        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([url])

                        pygame.mixer.music.set_volume(0.1)
                        engine.say('Playing ' + song)
                        engine.runAndWait()
                        

                        pygame.mixer.music.stop()
                        pygame.mixer.music.load('music/'+ytID+'.mp3')
                        pygame.mixer.music.play()

                    else:
                        pygame.mixer.music.set_volume(0.1)
                        engine.say('Playing ' + song)
                        engine.runAndWait()
                        

                        pygame.mixer.music.stop
                        pygame.mixer.music.load('music/'+ytID+'.mp3')
                        pygame.mixer.music.play()
                actualCommand = 1
            
            #Change The Wake Word
            elif 'change the wake word to' in cmd:
                reg_ex = re.search('change the wake word to (.+)', cmd)
                if reg_ex:
                    newWakeWord = reg_ex.group(1)

                    pygame.mixer.music.set_volume(0.1)
                    engine.say('Are you sure you want to change the wake word to ' + newWakeWord + ' ?')
                    engine.runAndWait()
                    
                    
                    change = 0
                    while change != 1:
                        wakeWordConfirm = myCommand()
                        
                        if 'yes' in wakeWordConfirm:
                            pygame.mixer.music.set_volume(0.1)

                            f = open("wakeWord.txt", "w")
                            f.write(newWakeWord)
                            f.close()
                            f = open("wakeWord.txt", "r")
                            wakeWord = f.read()
                            f.close
                            
                            confirmTxt = ('The wake word has been changed to', wakeWord)
                            print(confirmTxt)
                            engine.say(confirmTxt)
                            engine.runAndWait()
                            
                            change = 1
                            
                        elif 'no' in wakeWordConfirm:
                            pygame.mixer.music.set_volume(0.1)
                            confirmTxt = ('Ok the wake word will stay as', wakeWord)
                            engine.say(confirmTxt)
                            engine.runAndWait()
                            
                            change = 1
        
                        else:
                            pygame.mixer.music.set_volume(0.1)
                            engine.say('please answer yes or no. now try again.')
                            engine.runAndWait()

                        
                            
                actualCommand = 1

            #Help
            elif 'help' in cmd:
                pygame.mixer.music.set_volume(0.1)
                hello = 'Hello I am '+wakeWord+' your virtual assistant and here is a list of commands you can ask me to do.'
                helpMe = 'Say "'+wakeWord+' help", for me to list all the commands.'
                volume = 'Say "'+wakeWord+' volume" followed by a number between 0 and 10, to change the volume'
                mute = 'Say "'+wakeWord,' mute" or "'+wakeWord,' unmute", to mute or unmute me'
                joke = 'Say "'+wakeWord+' tell me a joke", and I will tell you a joke'
                tellDay = 'Say "'+wakeWord+' what day is it", and I will tell you the day'
                tellTime = 'Say "'+wakeWord+' what time is it", and I will tell you the time'
                openYT = 'Say "'+wakeWord+' open youtube", and I will open youtube for you'
                searchYT = 'Say "'+wakeWord+' search youtube for" followed by what you want to search, and I will open youtube and search for it'
                openWebsite = 'Say "'+wakeWord+' open the website" followed by the website, and I will open the website of your choice'
                subreddit = 'Say "'+wakeWord+' r / " then a subreddit of your choice, and I will open that subreddit'
                wiki = 'Say "'+wakeWord+' tell me about " then any subject of your choice, and I will tell you a bit about it'
                tellWeather = 'Say "'+wakeWord+' what\'s the current weather in" any city of your choice and I will tell you the weather, current temperature, maximum temperature and the minimumtemperature'
                changeWakeWord = 'Say "'+wakeWord+' change the wake word to" then any word slash phrase to change the wake word'
                playSong = 'Say "'+wakeWord+' play" then any song of your choice to play the song.'
                closeProgram = 'Say "'+wakeWord,' Goodbye" or "'+wakeWord,' Stop" to close the program'
                
                engine.say(hello)
                engine.say(helpMe)
                engine.say(volume)
                engine.say(mute)
                engine.say(joke)
                engine.say(tellDay)
                engine.say(tellTime)
                engine.say(openYT)
                engine.say(searchYT)
                engine.say(openWebsite)
                engine.say(subreddit)
                engine.say(wiki)
                engine.say(tellWeather)
                engine.say(changeWakeWord)
                engine.say(playSong)
                engine.say(closeProgram)
                engine.runAndWait()
                
                actualCommand = 1

            #Stop the program
            elif 'goodbye' in cmd:
                pygame.mixer.music.set_volume(0.1)
                engine.say('Goodbye')
                engine.runAndWait()
                

                sys.exit()

            #stop song
            elif 'stop' in cmd:
                pygame.mixer.music.stop()

                actualCommand = 1

            elif 'roar' in cmd:
                pygame.mixer.music.set_volume(1)
                pygame.mixer.music.play('sounds/roar.mp3')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(volume)

                actualCommand = 1

            elif 'like me' in cmd:
                engine.say('yes I think you are great')
                engine.runAndWait()

                actualCommand = 1

            else:
                pygame.mixer.music.set_volume(0.1)
                engine.say('I dont know that one, please try again')
                engine.runAndWait()


        pygame.mixer.music.set_volume(volume)

    elif 'intruder alert' in command:
        engine.setProperty('volume', 1)
        pygame.mixer.music.set_volume(1)
        engine.say ('welcome to the rice fields')
        engine.runAndWait()
        pygame.mixer.music.load('sounds/intruderAlert.mp3')
        pygame.mixer.music.play()

#Start up
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('JASPER v1.0')
pygame.display.flip()

time = t.hour,t.minute

pygame.mixer.music.set_volume(volume)
engine.setProperty('volume', volume)

engine.say ('I\'m your personal assistant' + wakeWord)
engine.say ('It is currently')
engine.say (time)
engine.say (today)
engine.runAndWait()

#loop to continue executing multiple commands
while True:
    assistant(myCommand())

for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
