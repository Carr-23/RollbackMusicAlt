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

# Constant
# Check name of user in order to choose correct path, since each computer has a different user
checkuser = getpass.getuser()

# Add the username to the path
screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\stageTest.png'

# Global
# Default stage select
default = True

# Sound file to stop from anywhere
soundFile = None

# Checks if the program is running
runCode = False

# Ends loop when closed
endLoop = True

def imageChanges():
    # Takes a screenshot of the current screen and saves it
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    # Loads screenshot to img
    img = cv2.imread(screenshotPath)

    # Changes resolution of screenshot and saves it, so all monitors are supported regardless of resolution
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)

    # Crops screenshot so its only stage selection
    crop = img[940:1080, 710:1210]
    cv2.imwrite(screenshotPath, crop)

    # Pass the final image to the OCR function to check it over
    finalImage = cv2.imread(screenshotPath)
    ocr(finalImage)

def ocr(img):
    #
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    #

    # OCR and passes the text to the stageMusic
    config = ('-l eng --oem 1 --psm 3')
    stage = pytesseract.image_to_string(img, config=config)
    stageMusic(stage)

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
    pafy.new('https://www.youtube.com/watch?v=' + results[0]['id']).getbestaudio().download('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\' + fullStageFolder + '\\' + results[0]['name'] + '.wav', quiet=False)

def stageMusic(stage):
    # If default stages are chosen, then only default songs play
    global soundFile
    if (default):
            if (stage == "Dream Land N64"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\DL.wav'))
               soundFile.play()
            elif (stage == "Fountain of Dreams"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\FOD.wav'))
               soundFile.play()
            elif (stage == "Pokémon Stadium"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\PS.wav'))
               soundFile.play()
            elif (stage == "Yoshi\'s Story"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\YS.wav'))
               soundFile.play()
            elif (stage == "Final Destination"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\FD.wav'))
               soundFile.play()
            elif (stage == "Battlefield"):
               soundFile = vlc.MediaPlayer(('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\BF.wav'))
               soundFile.play()

def startUpCheck():
    # Try to create main folder, but if it isn't it will just pass nothing
    try:
        os.mkdir(os.path.join('C:\\Users\\' + checkuser + '\\Documents', 'Rollback Music ALT'))
    except OSError as error:
        print()

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
            print()

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
        entry.delete(0, tk.END)

    def enterSearch(event):
        if (entry.get() != '' and stageFolder.get() != 'Stage'):
            ytSearch(entry.get(),stageFolder.get())
            entry.delete(0, tk.END)

    def createNewWin():
        newWin = tk.Toplevel(window)
        newWin.title("Options")
        newWin.geometry('300x150')
        newWin.resizable(False, False)

        folder = Button(newWin, text="Open Folder")
        folder.place(x=100, y=25)

        start = Button(newWin, text="Start Key")
        start.place(x=75, y=75)
        end = Button(newWin, text="End Key")
        end.place(x=175, y=75)

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


    entry = tk.Entry(window, width =50,bg = "white", fg = "black")
    entry.place(x=95, y=15)
    entry.insert(0, "Search")
    entry.bind("<FocusIn>",delSearch)
    entry.bind("<Return>",enterSearch)


    defCheck = BooleanVar()
    defaultCheck = Checkbutton(window, variable=defCheck,onvalue=False, offvalue=True, text="Default")
    defaultCheck.place(x=10,y=10)
    default = defCheck.get()


    stageFolder = StringVar()
    stageFolder.set('Stage')
    stageDrop = OptionMenu(window,stageFolder,'DL','FOD','PS','YS','FD','BF')
    stageDrop.place(x=505,y=7)


    option = Button(window,text="Options", command=createNewWin)
    option.place(x=530, y=220)


    startMusicCheck = Button(window,text=mainButtonName,height=3,width=10,command=musicPlayerRunner)
    startMusicCheck.place(x=250, y=100)


    frame.pack()

    window.protocol("WM_DELETE_WINDOW", close)

    while True:
        if runCode is True and keyboard.is_pressed('p'):
            if firstPress == 0:
                 imageChanges()
                 firstPress = 1
            else:
                 soundFile.stop()
                 firstPress = 0
                 time.sleep(1.5)

        if endLoop is True:
            window.update()
            window.update_idletasks()
        else:
            exit()

if __name__ == "__main__":
    # Checks to make sure default folders and files are there
    #startUpCheck()

    # Loads up the UI menu for the program
    UI()
    keyboard.wait('space')