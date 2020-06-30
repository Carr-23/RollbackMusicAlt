import getpass
import numpy as np
import cv2
import keyboard
import pyautogui
import pytesseract


def main():
    #Check name of user in order to choose correct path, since each computer has a different user
    checkuser = getpass.getuser()

    #Add the username to the path
    screenshotPath = 'C:\\Users\\' + checkuser + '\\Documents\\stageTest.png'

    #Waits for space to be hit, SHOULD happen after every game
    keyboard.wait('space')

    #Takes a screenshot of the current screen and saves it
    #myScreenshot = pyautogui.screenshot()
    #myScreenshot.save(screenshotPath)

    #Loads screenshot to img
    img = cv2.imread(screenshotPath)

    #Changes resolution of screenshot and saves it, so all monitors are supported regardless of resolution
    res = cv2.resize(img, (1920,1080))
    cv2.imwrite(screenshotPath, res)

    #Crops screenshot so its only stage selection
    crop = img[940:1080,710:1210]
    cv2.imwrite(screenshotPath, crop)

    finalImage = cv2.imread(screenshotPath)

    config = ('-l eng --oem 1 --psm 3')
    text = pytesseract.image_to_string(finalImage, config = config)
test
if __name__ == "__main__":
    main()
