import getpass
import cv2
import keyboard
import pyautogui
from fast_youtube_search import search_youtube
import os
import pytesseract
import pafy
import vlc
import tkinter as tk
from tkinter import *
import time
import random
import numpy as np

# Constant
# Check name of user in order to choose correct path, since each computer has a different user
checkuser = getpass.getuser()

# Add the username to the path
screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\stageTest.png'

# Global

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
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    # Loads screenshot to img
    img = cv2.imread(screenshotPath)

    # Changes resolution of screenshot and saves it, so all monitors are supported regardless of resolution
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)

    # Crops screenshot so its only stage selection
    crop = img[940:1080, 660:1260]
    cv2.imwrite(screenshotPath, crop)

    # Pass the final image to the OCR function to check it over
    finalImage = cv2.imread(screenshotPath)
    ocr(finalImage,default)

def gameImageChanges():

    # Takes a screenshot of the current screen and saves it
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    img = cv2.imread(screenshotPath)
    img = cv2.resize(img, (1920, 1080))
    img = img[340:640, 500:1300]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (5, 5))
    img = cv2.medianBlur(img,5)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    img = cv2.bilateralFilter(img, 9, 75, 75)
    kernel = np.ones((5,5),np.uint8)
    img = cv2.dilate(img, kernel, iterations = 1)
    img = cv2.erode(img, kernel, iterations = 1)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    ret, img = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY_INV)

    cv2.imwrite(screenshotPath, img)

    # Pass the final image to the OCR function to check it over
    ocr(cv2.imread(screenshotPath),True)

def ocr(img,default):
    #
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #

    # OCR and passes the text to the stageMusic
    config = ('--oem 1 --psm 7 --psm 8 --psm 13 --psm 12')
    stage = pytesseract.image_to_string(img, lang='eng', config=config)
    print(stage)
    #stageMusic(stage,default)

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

def stageMusic(stage,default):
    # If default stages are chosen, then only default songs play
    global soundFile
    global playing
    if (stage == "Dream Land N64"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\DL.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage == "Fountain of Dreams"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\FOD.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage == "Pokémon Stadium"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\PS.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage == "Yoshi\'s Story"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\YS.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage == "Final Destination"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\FD.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage == "Battlefield"):
        if (not default):
            soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\BF.wav'))
        else:
            files = os.listdir('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield')
            soundFile = vlc.MediaPlayer('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\' + random.choice(files))
        soundFile.play()
        playing = True
    elif (stage != '' and stage == 'Game'):
        soundFile.stop()
        playing = False

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
            pafy.new('https://www.youtube.com/watch?v=' + defaultIDS[x]).getbestaudio().download(path[x] + '\\' + acro[x] + '.wav',quiet=False)


    ##############################################
    # ^ Folders and Default Music. CONFIG File v #
    ##############################################

    try:
        configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "r+")
    except IOError as error:
        configFile.write('[Variable]	Default 	Volume 		Auto 		Delay 		Input\n')
        configFile.write('[Value]		False 		100 		False 		0.016 		p\n')
        configFile.write('[Description]	(T/F) 		(0<x<100)	(T/F)		(0.016<x<30)	(key)')

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

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def UI():

    # Checks for first and second inputs to be active or not
    firstPress = 0

    # The name of the main button
    mainButtonName = "RUN"

    window = tk.Tk()
    window.title("Rollback Music ALT")
    window.geometry('600x260')
    window.resizable(False, False)

    #######################################

    def delSearch(event):
        if (entry.get() == 'Search'):
            entry.delete(0, tk.END)

    def reSearch(event):
        if (entry.get() == ''):
            entry.insert(0, "Search")

    def enterSearch(event):
        if (entry.get() != '' and stageFolder.get() != 'Stage'):
            ytSearch(entry.get(),stageFolder.get())
            entry.delete(0, tk.END)

    def openFolder():
        os.startfile('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT')

    def changeKey():
        global keyToStart
        k = keyboard.read_key()
        if k != 'esc':
            keyToStart = k

    def createNewWin():

        ####################################

        def enterValue(event):
            global delay
            if (is_number(delayEntry.get()) and float(delayEntry.get()) >= 0.015 and float(delayEntry.get()) <= 30):
                delay = delayEntry.get()
                newWin.focus()
            else:
                delayEntry.delete(0, tk.END)
                delayEntry.insert(0, str(delay))

        def changeLabel():
            changeKey()
            start.config(text="Set Input Key [" + keyToStart +"]")

        ####################################


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


    entry = Entry(window, width =50,bg = "white", fg = "black")
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
        if autoCheck.get() is False:
            if runCode is True and keyboard.is_pressed(keyToStart):
                if firstPress == 0:
                     imageChanges(defCheck.get())
                     firstPress = 1
                else:
                     soundFile.stop()
                     firstPress = 0
                     time.sleep(1.5)
            elif runCode is False and firstPress == 1:
                soundFile.stop()
                firstPress = 0
                time.sleep(1.5)
            elif runCode is True and firstPress == 1:
                soundFile.audio_set_volume(vol.get())
        else:
            if runCode is True and playing is False:
                imageChanges()
                time.sleep(delay)
            elif runCode is True and playing is True:
                gameImageChanges()
                time.sleep(delay)
            elif runCode is True and playing is True and keyboard.is_pressed('esc'):
                soundFile.stop()
                global playing
                playing = False
                time.sleep(1.5)
            elif runCode is False and playing is True:
                soundFile.stop()
                global playing
                playing = False
                time.sleep(1.5)

        if endLoop is True:
            window.update()
            window.update_idletasks()
        else:
            configFile = open('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\CONFIG.txt', "w+")
            configFile.write('[Variable]	Default 	Volume 		Auto 		Delay 		Input\n')
            configFile.write('[Value]		' + str(defCheck.get()) + ' 		' + str(vol.get()) + ' 		' + str(autoCheck.get()) + ' 		' + str(delay) + ' 		' + str(keyToStart) + '\n')
            configFile.write('[Description]	(T/F) 		(0<x<100)	(T/F)		(0.016<x<30)	(key)')
            exit()

if __name__ == "__main__":

    # Checks to make sure default folders and files are there
    #startUpCheck()
    # Loads up the UI menu for the program
    #UI()
    gameImageChanges()



# Left to do
# - Automation
