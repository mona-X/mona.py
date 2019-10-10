from os import walk, getenv, system
from shutil import copyfile

image = "screen.jpg"

appdata = getenv("APPDATA")
dst = appdata + "\Microsoft\Windows\Themes"

for root2, dirs2, files2 in walk(dst):
    for files2 in files2:
        if files2.endswith((".jpg")):
            copyfile(image, files2)
        copyfile(image,dst+"\TranscodeWallpaper")

system("taskkill /f /im explorer.exe")
system("C:\Windows\explorer.exe")
