import getpass
import cv2
import keyboard
import pyautogui
from fast_youtube_search import search_youtube
import os
import pytesseract
import pafy
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
#os.environ['OMP_THREAD_LIMIT'] = '1'
import vlc
import tkinter as tk
from tkinter import *
import time
import random
import numpy as np
from PIL import Image
import math
# Constant
# Check name of user in order to choose correct path, since each computer has a different user
checkuser = getpass.getuser()

# Add the username to the path
screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\stageScreenShot.png'

# Global

# start time and end time
startTime = None

# Length of sound
soundDuration = None

# Sound file path
soundFilePath = None

# Sound file to stop from anywhere
soundFile = None

# Checks if the program is running
runCode = False

# Ends loop when closed
endLoop = True

# The key you press to start and stop the playing
keyToStart = None

# Check to see if it will be automatic or not
auto = None

# delay
delay = None

# Custom or Default songs
default = None

# Volume level
volume = None

# playing music
playing = False


def imageChanges(default):
    # Takes a screenshot of the current screen and saves it
    myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    # Loads screenshot to img
    #img = cv2.imread(screenshotPath)
    open_cv_image = np.array(myScreenshot)
    img = open_cv_image[:, :, ::-1].copy()

    # Changes resolution of screenshot and saves it, so all monitors are supported regardless of resolution
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)

    # Crops screenshot so its only stage selection
    crop = img[940:1080, 660:1260]
    ret, final1 = cv2.threshold(crop, 150, 255, cv2.THRESH_BINARY_INV)

    # Pass the final image to the OCR function to check it over
    ocr(final1,default)
def gameImageChanges():

    # Takes a screenshot of the current screen and saves it
    myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    # Loads screenshot to img
    #img = cv2.imread(screenshotPath)
    open_cv_image = np.array(myScreenshot)
    img = open_cv_image[:, :, ::-1].copy()

    # Changes resolution of screenshot and saves it, so all monitors are supported regardless of resolution
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)

    im = Image.open(screenshotPath)
    pix = im.load()
    # Check Pixels
    if (pix[514,460] <= (255,255,255) and pix[514,460] >= (205,205,205) and
    pix[666,420] <= (50,50,50) and pix[666,420] >= (0,0,0) and
    pix[630,500] <= (98,31,36) and pix[630,500] >= (13,0,0) and
    pix[1340,600] <= (255,194,169) and pix[1340,600] >= (223,142,117) and
    pix[1070,550] <= (246,27,38) and pix[1070,550] >= (194,0,0)):
        stageMusic('Game',True)

    elif (pix[530,350] <= (217,209,192) and pix[530,350] >= (167,159,142) and #Grey
    pix[610,410] <= (60,50,50) and pix[610,410] >= (10,0,0) and #Red
    pix[415,340] <= (74,81,171) and pix[415,340] >= (24,31,121) and #Blue
    pix[1515,320] <= (50,239,50) and pix[1480,320] >= (0,189,0) and #Green
    pix[820,375] <= (131,98,255) and pix[820,375] >= (81,48,230) and #Purple
    pix[820,490] <= (57,148,121) and pix[820,490] >= (7,98,71)): # Teal
        stageMusic('EVENT',True)
    else:
        pass
        #crop = res[75:115, 425:565]
        #final = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
        #pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        #config = ('--oem 1 --psm 7 --psm 8 --psm 13 --psm 12')
        #stage1 = pytesseract.image_to_string(final, lang='eng', config=config)
        #stage = ' '.join(stage1.split())
        #stageMusic(stage,True)

def ocr(img,default):
    # Location of tesseract,exe
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    #

    # OCR and passes the text to the stageMusic
    config = ('--oem 1 --psm 7')
    stage = pytesseract.image_to_string(img, lang='eng', config=config)
    stageMusic(stage,default)

def ytSearch(searchTerm,folder):
    # Takes a text and splits each word. Searches the list and outputs the information for the video
    results = search_youtube(searchTerm.split())
    if folder == 'DL':
        fullStageFolder = 'Dream Land N64'
    elif folder == 'FOD':
        fullStageFolder = 'Fountain of Dreams'
    elif folder == 'PS':
        fullStageFolder = 'Pokémon Stadium'
    elif folder == 'YS':
        fullStageFolder = 'Yoshi\'s Story'
    elif folder == 'FD':
        fullStageFolder = 'Final Destination'
    elif folder == 'BF':
        fullStageFolder = 'Battlefield'

    # Replaces characters that isn't supported in Windows naming for files
    for char in results[0]['name']:
        if char in "<>:\"/\\|?*":
            results[0]['name'] = results[0]['name'].replace(char, '')

    # Takes the ID of the video to find the proper youtube URL to download
    pafy.new('https://www.youtube.com/watch?v=' + results[0]['id']).getbestaudio().download('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\' + fullStageFolder + '\\' + results[0]['name'] + '.wav', quiet=True)

def stageMusic(stage1,default):

    def split(word):
        return [char for char in word]

    # If default stages are chosen, then only default songs play
    global soundFile
    global soundFilePath
    global playing
    global startTime

    stage = ' '.join(stage1.split())
    stage2 = ' '.join(stage1.split())
    #print(stage)
    stage = stage.replace(' ','')
    stage = stage.lower()
    stage = split(stage)
    if len(stage) >= math.ceil(len("Dream Land N64")*0.75) and (all(x in "dream land n64" for x in stage)) and not playing:
        if (default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\DL.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif len(stage) >= math.ceil(len("Fountain of Dreams")*0.75) and (all(x in "fountain of dreams" for x in stage)) and not playing:
        if (default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\FOD.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif len(stage) >= math.ceil(len("Pokémon Stadium e")*0.75) and (all(x in "pokémon stadium e" for x in stage)) and not playing:
        if (default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\PS.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif len(stage) >= math.ceil(len("Yoshi\'s Story")*0.75) and (all(x in "yoshi\'s story" for x in stage)) and not playing:
        if (not default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\YS.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif len(stage) >= math.ceil(len("Final Destination")*0.75) and (all(x in "final destination" for x in stage)) and not playing:
        if (default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\FD.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif len(stage) >= math.ceil(len("Battlefield")*0.75) and (all(x in "battlefield" for x in stage)) and not playing:
        if (default):
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\BF.wav')
            soundFile = vlc.MediaPlayer(soundFilePath)
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield')
            soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\' + random.choice(files))
            soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
    elif (stage2 == "Game") and playing:
        soundFile.stop()
        playing = False
    elif (stage2 == "EVENT") and playing:
        soundFile.stop()
        playing = False
    else:
        pass
def startUpCheck():
    # Try to create main folder, but if it isn't it will just pass nothing
    try:
        os.mkdir(os.path.join('C:\\Users\\' + checkuser + '\\Documents', 'Rollback Music ALT'))
    except OSError as error:
        pass

    # Path for all the folders inside main folder
    generalPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT'

    # All the names of the folders in the main folder
    path = [
            os.path.join(generalPath, 'Dream Land N64'),
            os.path.join(generalPath, 'Fountain of Dreams'),
            os.path.join(generalPath, 'Pokémon Stadium'),
            os.path.join(generalPath, 'Yoshi\'s Story'),
            os.path.join(generalPath, 'Final Destination'),
            os.path.join(generalPath, 'Battlefield'),
            os.path.join(generalPath, '0Temp')
            ]

    # Creates the folders, unless they arleady exist
    for x in range(7):
        try:
            os.mkdir(path[x])
        except OSError as error:
            pass

    # ID's for the defualt songs
    defaultIDS = [
                  '40SjNtbuNYU',
                  'pz3BQFXjEOI',
                  'mS8-zZ9EZCA',
                  'EcHiSeA57TU',
                  'L8EfpcF9rRc',
                  'u72SLGULM8A'
                 ]
    # Acronyms for the stages
    acro = ['DL','FOD','PS','YS','FD','BF']

    # Download music unless they already exist
    for x in range(6):
        if (not(os.path.isfile(path[x] + '\\' + acro[x] + '.wav'))):
            pafy.new('https://www.youtube.com/watch?v=' + defaultIDS[x]).getbestaudio().download(path[x] + '\\' + acro[x] + '.wav',quiet=True)


    ##############################################
    # ^ Folders and Default Music. CONFIG File v #
    ##############################################

    try:
        configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "r+")
    except IOError as error:
        configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "w")
        configFile.write('[Variable]	Default 	Volume 		Auto 		Delay 		Input\n')
        configFile.write('[Value]		False 		100 		False 		0.016 		p\n')
        configFile.write('[Description]	(T/F) 		(0<x<100)	(T/F)		(0.016<x<30)	(key)')
        configFile.close()
        configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "r+")

    lines = configFile.readlines()
    if len(lines) != 3 or len(lines[1].split()) != 6 or lines[1].split()[0] != '[Value]':
        configFile.write('[Variable]	Default 	Volume 		Auto 		Delay 		Input\n')
        configFile.write('[Value]		False 		100 		False 		0.016 		p\n')
        configFile.write('[Description]	(T/F) 		(0<x<100)	(T/F)		(0.016<x<30)	(key)')

    fileValues=lines[1].split()
    global keyToStart,auto,default,volume,delay
    keyToStart = fileValues[5]
    if is_number(fileValues[4]): delay = float(fileValues[4])
    auto = (fileValues[3])
    if is_number(fileValues[2]): volume = int(fileValues[2])
    default = (fileValues[1])

    if delay < 0.016 or delay>30:
        delay = 0.016

    if auto == "True":
        auto = True
    else:
        auto = False

    if volume<0 or volume>100:
        volume = 100

    if default == "True":
        default = True
    else:
        default = False

#Checks to see if it is a valid float number
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

# Gets Duration of Songs
def getDuration(path):
    instance = vlc.Instance()
    media = instance.media_new(path)
    media.parse_with_options(1, 0)
    while True:
        if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
            break
    return media.get_duration()

# Shitty User Interface
def UI():

    # Checks for first and second inputs to be active or not
    firstPress = 0

    # The name of the main button
    mainButtonName = "RUN"

    global playing

    # Creates default window
    window = tk.Tk()
    window.title("Rollback Music ALT")
    window.geometry('600x260')
    window.resizable(False, False)

    #######################################

    # Deletes Search bar when clicked
    def delSearch(event):
        if (entry.get() == 'Search'):
            entry.delete(0, tk.END)

    # Wont submit the search entry if it is blank
    def reSearch(event):
        if (entry.get() == ''):
            entry.insert(0, "Search")

    # Sends the search entry to download the youtube video
    def enterSearch(event):
        if (entry.get() != '' and stageFolder.get() != 'Stage'):
            ytSearch(entry.get(),stageFolder.get())
            entry.delete(0, tk.END)

    # Open the specific folder in file explorer
    def openFolder():
        os.startfile('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT')

    # Change the key for the manual function
    def changeKey():
        global keyToStart
        k = keyboard.read_key()
        if k != 'esc':
            keyToStart = k

    # Creates the secondary window
    def createNewWin():

        ####################################

        # Change delay
        def enterValue(event):
            global delay
            if (is_number(delayEntry.get()) and float(delayEntry.get()) >= 0.015 and float(delayEntry.get()) <= 30):
                delay = delayEntry.get()
                newWin.focus()
            else:
                delayEntry.delete(0, tk.END)
                delayEntry.insert(0, str(delay))

        # Change label for key to start
        def changeLabel():
            changeKey()
            start.config(text="Set Input Key [" + keyToStart +"]")

        ####################################

        # V - User Interface - V
        newWin = tk.Toplevel(window)
        newWin.title("Options")
        newWin.geometry('300x150')
        newWin.resizable(False, False)

        folder = Button(newWin, text="Open Folder", command=openFolder)
        folder.place(relx=0.5, rely=0.2, anchor=CENTER)

        start = Button(newWin, text="Set Input Key [" + keyToStart +"]", command=changeLabel)
        start.place(relx=0.5, rely=0.5, anchor=CENTER)

        entryLabel = Label(newWin,text="Delay :")
        entryLabel.place(relx=0.38, rely=0.8, anchor=CENTER)

        delayEntry = Entry(newWin, width =7,bg = "white", fg = "black", justify = CENTER)
        delayEntry.insert(0, delay)
        delayEntry.place(relx=0.57, rely=0.8, anchor=CENTER)
        delayEntry.bind("<Return>", enterValue)

        newWin.transient(window)
        newWin.grab_set()
        window.wait_window(newWin)

    def musicPlayerRunner():
        global runCode
        if (runCode is False):
            startMusicCheck.config(text="END")
            runCode = True
        else:
            startMusicCheck.config(text="RUN")
            runCode = False;

    def close():
        global endLoop
        endLoop = False

    #######################################

    frame = Frame(window, width=600, height=260)
    frame.bind("<1>", lambda event: frame.focus_set())


    entry = Entry(window, width = 65,bg = "white", fg = "black")
    entry.place(x=95, y=15)
    entry.insert(0, "Search")
    entry.bind("<FocusIn>",delSearch)
    entry.bind("<FocusOut>",reSearch)
    entry.bind("<Return>",enterSearch)

    vol = IntVar()
    volumeScale = Scale(window,from_=100,to=0,orient=HORIZONTAL,length=150, showvalue = 1, variable = vol)
    volumeScale.set(volume)
    volumeScale.place(relx=0.15, rely=0.9, anchor=CENTER)


    defCheck = BooleanVar()
    defCheck.set(default)
    defaultCheck = Checkbutton(window, variable=defCheck,onvalue=True, offvalue=False, text="Default")
    defaultCheck.place(x=10,y=10)


    stageFolder = StringVar()
    stageFolder.set('Stage')
    stageDrop = OptionMenu(window,stageFolder,'DL','FOD','PS','YS','FD','BF')
    stageDrop.place(x=505,y=7)


    option = Button(window,text="Options", command=createNewWin)
    option.place(x=530, y=220)


    startMusicCheck = Button(window,text=mainButtonName,height=3,width=10,command=musicPlayerRunner)
    startMusicCheck.place(relx=0.5, rely=0.5, anchor=CENTER)


    autoCheck = BooleanVar()
    autoCheck.set(auto)
    autCheck = Checkbutton(window, variable=autoCheck,onvalue=True, offvalue=False, text="Auto")
    autCheck.place(relx=0.5, rely=0.75, anchor=CENTER)


    frame.pack()

    window.protocol("WM_DELETE_WINDOW", close)

    while True:
        global startTime
        global soundFilePath
        global soundFile
        # Manual Music Player
        if not autoCheck.get():
            # Checks the information using OCR to determin if the song should be played with manual start key
            if runCode and keyboard.is_pressed(keyToStart):
                if firstPress == 0:
                     imageChanges(defCheck.get())
                     firstPress = 1
                     time.sleep(1.5)
                     volumeStart = vol.get()
                else:
                     soundFile.stop()
                     firstPress = 0
                     time.sleep(1.5)
            # Kill switch using the main button
            elif not runCode and firstPress == 1:
                soundFile.stop()
                firstPress = 0
                time.sleep(1)
            elif runCode and firstPress == 1:
                # Changes the volume if changed
                if volumeStart != vol.get():
                    soundFile.audio_set_volume(vol.get())
                    volumeStart = vol.get()
                # Replays the song after it is done
                if ((int(round(time.time() * 1000))) - (startTime)) >= getDuration(soundFilePath):
                    time.sleep(0.05)
                    soundFile = vlc.MediaPlayer(soundFilePath)
                    soundFile.play()
                    startTime = int(round(time.time() * 1000))
                    time.sleep(1.5)

        # Automatic Music Player
        else:
            # Checks the information using OCR to determin if the song should be played
            if runCode and not playing:
                imageChanges(defCheck.get())
                time.sleep(delay)
                volumeStart = vol.get()
            # Kill switch using esc key
            elif runCode and playing and keyboard.is_pressed('space'):
                soundFile.stop()
                playing = False
                time.sleep(1)
            # Changes the volume if changed
            elif runCode and playing:
                if volumeStart != vol.get():
                    soundFile.audio_set_volume(vol.get())
                    volumeStart = vol.get()
                # Replays the song after it is done
                if ((int(round(time.time() * 1000))) - (startTime)) >= getDuration(soundFilePath):
                    time.sleep(0.05)
                    soundFile = vlc.MediaPlayer(soundFilePath)
                    soundFile.play()
                    startTime = int(round(time.time() * 1000))
                    time.sleep(1.5)
                # Checks if the game is done to end the song
                gameImageChanges()
                time.sleep(delay)
            # Kill switch using the main button
            elif not runCode and playing:
                soundFile.stop()
                playing = False
                time.sleep(1)

        # Runs the program in loop
        if endLoop:
            window.update()
            window.update_idletasks()
        else:
            configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "w+")
            configFile.write('[Variable]	Default 	Volume 		Auto 		Delay 		Input\n')
            configFile.write('[Value]		' + str(defCheck.get()) + ' 		' + str(vol.get()) + ' 		' + str(autoCheck.get()) + ' 		' + str(delay) + ' 		' + str(keyToStart) + '\n')
            configFile.write('[Description]	(T/F) 		(0<x<100)	(T/F)		(0.016<x<30)	(key)')
            break
def main():
    # Checks to make sure default folders and files are there
    startUpCheck()
    # Loads up the UI menu for the program
    UI()

if __name__ == "__main__":
    main()

# Lower Case
# Nicer UI
# Create maybe a lite version
