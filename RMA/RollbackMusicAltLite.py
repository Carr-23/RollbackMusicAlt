import getpass
import cv2
import pyautogui
from fast_youtube_search import search_youtube
import os
import pytesseract
import pafy
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
import vlc
import time
import random
import numpy as np
from PIL import Image
import math
checkuser = getpass.getuser()
screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\stageScreenShot.png'

startTime = None

soundDuration = None

soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\DL.wav')

soundFile = None

playing = False


def imageChanges():
    myScreenshot = pyautogui.screenshot()
    open_cv_image = np.array(myScreenshot)
    img = open_cv_image[:, :, ::-1].copy()
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)
    crop = img[940:1080, 660:1260]
    ret, final1 = cv2.threshold(crop, 150, 255, cv2.THRESH_BINARY_INV)
    ocr(final1)

def gameImageChanges():
    myScreenshot = pyautogui.screenshot()
    open_cv_image = np.array(myScreenshot)
    img = open_cv_image[:, :, ::-1].copy()
    res = cv2.resize(img, (1920, 1080))
    cv2.imwrite(screenshotPath, res)

    im = Image.open(screenshotPath)
    pix = im.load()
    if (pix[514,460] <= (255,255,255) and pix[514,460] >= (205,205,205) and
    pix[666,420] <= (50,50,50) and pix[666,420] >= (0,0,0) and
    pix[630,500] <= (98,31,36) and pix[630,500] >= (13,0,0) and
    pix[1340,600] <= (255,194,169) and pix[1340,600] >= (223,142,117) and
    pix[1070,550] <= (246,27,38) and pix[1070,550] >= (194,0,0)):
        stageMusic('Game')

    elif (pix[530,350] <= (217,209,192) and pix[530,350] >= (167,159,142) and #Grey
    pix[610,410] <= (60,50,50) and pix[610,410] >= (10,0,0) and #Red
    pix[415,340] <= (74,81,171) and pix[415,340] >= (24,31,121) and #Blue
    pix[1515,320] <= (50,239,50) and pix[1480,320] >= (0,189,0) and #Green
    pix[820,375] <= (131,98,255) and pix[820,375] >= (81,48,230) and #Purple
    pix[820,490] <= (57,148,121) and pix[820,490] >= (7,98,71)): # Teal
        stageMusic('EVENT')
    else:
        pass

def ocr(img):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
    config = ('--oem 1 --psm 7')
    stage = pytesseract.image_to_string(img, lang='eng', config=config)
    stageMusic(stage)

def stageMusic(stage1):

    def split(word):
        return [char for char in word]

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
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Dream Land N64\\DL.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif len(stage) >= math.ceil(len("Fountain of Dreams")*0.75) and (all(x in "fountain of dreams" for x in stage)) and not playing:
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Fountain of Dreams\\FOD.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif len(stage) >= math.ceil(len("Pokémon Stadium e")*0.75) and (all(x in "pokémon stadium e" for x in stage)) and not playing:
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Pokémon Stadium\\PS.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif len(stage) >= math.ceil(len("Yoshi\'s Story")*0.75) and (all(x in "yoshi\'s story" for x in stage)) and not playing:
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Yoshi\'s Story\\YS.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif len(stage) >= math.ceil(len("Final Destination")*0.75) and (all(x in "final destination" for x in stage)) and not playing:
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Final Destination\\FD.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif len(stage) >= math.ceil(len("Battlefield")*0.75) and (all(x in "battlefield" for x in stage)) and not playing:
        soundFilePath = ('C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\Battlefield\\BF.wav')
        soundFile = vlc.MediaPlayer(soundFilePath)
        time.sleep(0.05)
        soundFile.play()
        startTime = int(round(time.time() * 1000))
        playing = True
        #print('Playing...')
    elif (stage2 == "Game") and playing:
        soundFile.stop()
        playing = False
        #print('Ending...')
    elif (stage2 == "EVENT") and playing:
        soundFile.stop()
        playing = False
        #print('Ending...')
    else:
        pass

def startUpCheck():
    try:
        os.mkdir(os.path.join('C:\\Users\\' + checkuser + '\\Documents', 'Rollback Music ALT'))
    except OSError as error:
        pass

    generalPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT'

    path = [
            os.path.join(generalPath, 'Dream Land N64'),
            os.path.join(generalPath, 'Fountain of Dreams'),
            os.path.join(generalPath, 'Pokémon Stadium'),
            os.path.join(generalPath, 'Yoshi\'s Story'),
            os.path.join(generalPath, 'Final Destination'),
            os.path.join(generalPath, 'Battlefield'),
            os.path.join(generalPath, '0Temp')
            ]

    for x in range(7):
        try:
            os.mkdir(path[x])
        except OSError as error:
            pass

    defaultIDS = [
                  '40SjNtbuNYU',
                  'pz3BQFXjEOI',
                  'mS8-zZ9EZCA',
                  'EcHiSeA57TU',
                  'L8EfpcF9rRc',
                  'u72SLGULM8A'
                 ]
    acro = ['DL','FOD','PS','YS','FD','BF']

    for x in range(6):
        if (not(os.path.isfile(path[x] + '\\' + acro[x] + '.wav'))):
            pafy.new('https://www.youtube.com/watch?v=' + defaultIDS[x]).getbestaudio().download(path[x] + '\\' + acro[x] + '.wav',quiet=True)

def getDuration(path):
    instance = vlc.Instance()
    media = instance.media_new(path)
    media.parse_with_options(1, 0)
    while True:
        if str(media.get_parsed_status()) == 'MediaParsedStatus.done':
            break
    return media.get_duration()

def UI():
    while True:
        global startTime
        global soundFilePath
        global soundFile
        if not playing:
            imageChanges()
            time.sleep(0.017)
            dur = getDuration(soundFilePath)
        elif playing:
            if ((int(round(time.time() * 1000))) - (startTime)) >= dur:
                time.sleep(0.05)
                soundFile = vlc.MediaPlayer(soundFilePath)
                soundFile.play()
                startTime = int(round(time.time() * 1000))
                time.sleep(1.5)
            gameImageChanges()
            time.sleep(0.017)
def main():
    startUpCheck()
    UI()

if __name__ == "__main__":
    main()
