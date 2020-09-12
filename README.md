# Rollback Music Alternative

Our God Fizzi created, [Rollback Netcode](https://slippi.gg/) for the beloved GameCube game 'Super Smash Bros. Melee'.
However, with all the greatness that came there was one small flaw which was NO-MUSIC.

Sadly, many people miss the Dreamland chants!

There is a solution however it is not the most optimal.
What [RollbackMusicAlt](https://github.com/Carr-23/RollbackMusicAlt/releases/tag/1.1) does is it detects what stage you're playing on based on your display, and then plays the respected songs for that stage.

P.S. this was my first time coding in Python and was the project that I used to learn the language

## Getting Started

### [UI RollbackMusicAlt](https://github.com/Carr-23/RollbackMusicAlt/releases/tag/1.1)

1. **Default Checkbox** -> used to change between default stage music or a custom playlist
2. **Searchbar** -> allows you to search for anything and it will download the first YouTube video to the corresponding stage playlist
3. **Stage Playlist Dropdown** -> choose which stage playlist the YouTube video will be downloaded to
4. **Run Button** -> this will start the main function of RollbackMusicAlt (for automated you can press 'space' as a kill switch also)
5. **Auto Checkbox** -> used to change between manual and automated music player (automated works best)
6. **Volume Level** -> allows you to change the musics volume
7. **Option Tab** -> open the option window

![](/images/rollbackPlayer.png)

1. **Open Folder** -> opens the folder were everything is stored
2. **Set Input Key** -> lets you set an input for the manual start function (press key to start during loading screen and press to end)
3. **Delay Input** -> allows you to choose how often it checks for a change on the display (0.016 ≈ Every Frame)

![](/images/option.png)

### [No UI RollbackMusicAltLite](https://github.com/Carr-23/RollbackMusicAlt/releases/tag/1.0-Lite)

You only have to double click the .exe and once that happens this black window will appear to let you know it is running. To shut it off, just close the window.

![](/images/RollbackMusicAltLiteRunning.png)

## Installing

### Prerequisites
Make sure you have the following installed:

**Install** [VLC - 64 bit](https://www.videolan.org/vlc/download-windows.html) inside 'C:\Program Files\VideoLAN\VLC'

![](images/vlc.PNG)

**Install** [Tesseract-OCR](https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows) inside 'C:\Program Files (x86)\Tesseract-OCR\'

![](/images/tesseract.PNG)

**Install** [Python - 64 bit](https://www.python.org/downloads/windows/)

![](/images/python.PNG)

### Download

You can download V1.1 here: [RollbackMusicAlt](https://github.com/Carr-23/RollbackMusicAlt/releases/tag/1.1)

You can download V1.0-Lite here: [RollbackMusicAlt](https://github.com/Carr-23/RollbackMusicAlt/releases/tag/1.0-Lite)

![](/images/rollback.PNG)

## Built With

* [getPass](https://docs.python.org/3/library/getpass.html)        - Used to get current Windows 10 user
* [OpenCV](https://pypi.org/project/opencv-python/)                    - Used to edit the screenshot
* [keyboard](https://pypi.org/project/keyboard/)          - Used to get user input
* [pyautogui](https://pypi.org/project/PyAutoGUI/)         - Used to screenshot
* [pytesseract](https://pypi.org/project/pytesseract/)       - Used to convert the image to text (OCR)
* [fast_youtube_search](https://pypi.org/project/fast-youtube-search/)       - Used to get YouTube search results
* [os](https://pythonprogramming.net/python-3-os-module/)       - Used to manage files
* [pafy](https://pypi.org/project/pafy/)       - Used to download YouTube Videos
* [vlc](https://pypi.org/project/python-vlc/)       - Used to run Music
* [tkinter](https://tkdocs.com/tutorial/install.html)       - Used to create the user interface
* [numpy](https://pypi.org/project/numpy/)       - Used for OCR image processing
* [youtube-dl](https://pypi.org/project/youtube_dl/) - Used as a part of pafy
* [Pillow](https://pypi.org/project/Pillow/2.2.2/) - Used to read pixel data


## Versioning

#### Normal

* 1.0 -> Launch
* 1.1 -> Fix Lag issue

#### Lite

* 1.0 -> It's normal 1.1 without a UI

## Authors

* **Braulio Carrion Corveira** - *Future Computer Engineer* - Outdated Site: https://carr-23.github.io/

## Future Builds
- Better UI with a custom look
- Drag and drop URL's
- Fix lag when changing input key
- Fix issue of no music playing even if detected (no idea how to fix as of now)

## Looking To Help Out?

The main things I would need help with is optimizing the code, and creating a better User interface.
You can contact me on my throwaway email: gone.pokemon@gmail.com

## Acknowledgments

* Go support Fizzi at https://slippi.gg/
* After Supporting Fizzi, if you still want to support me you can do so at https://paypal.me/brauliocarr

