import getpass
import cv2
import keyboard
import pyautogui
from fast_youtube_search import search_youtube
import os
import pytesseract
import pafy

def imageChanges():
    # Takes a screenshot of the current screen and saves it
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(screenshotPath)

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
    #stageMusic(stage)

def ytSearch():
    results = search_youtube('idk'.split())
    print('https://www.youtube.com/watch?v=' + results[0]['id'])

def startUpCheck():
    try:
        os.mkdir(os.path.join('C:\\Users\\' + checkuser + '\\Documents', 'Rollback Music ALT'))
    except OSError as error:
        print()

    generalPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT'

    path = [
            os.path.join(generalPath, 'Dream Land N64 - Music'),
            os.path.join(generalPath, 'Fountain of Dream - Music'),
            os.path.join(generalPath, 'Pokémon Stadium - Music'),
            os.path.join(generalPath, 'Yoshi\'s Story - Music'),
            os.path.join(generalPath, 'Final Destination - Music'),
            os.path.join(generalPath, 'Battlefield - Music'),
            os.path.join(generalPath, '0Temp')
            ]

    for x in range(7):
        try:
            os.mkdir(path[x])
        except OSError as error:
            print()

    defaultIDS = [
                  '40SjNtbuNYU',
                  'pz3BQFXjEOI',
                  'mS8-zZ9EZCA',
                  'EcHiSeA57TU',
                  'L8EfpcF9rRc',
                  'u72SLGULM8A'
                 ]
    for x in range(6):
        pafy.new('https://www.youtube.com/watch?v=' + defaultIDS[x]).getbestaudio().download(generalPath + path[x])

if __name__ == "__main__":

    # Check name of user in order to choose correct path, since each computer has a different user
    checkuser = getpass.getuser()

    # Add the username to the path
    screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\Rollback Music ALT\\0Temp\\stageSS.png'

    startUpCheck()

    # Waits for space to be hit, SHOULD happen after every game
    keyboard.wait('space')
    imageChanges()
    print("test")