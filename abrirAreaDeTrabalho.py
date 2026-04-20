import os
import webbrowser
import time


# Opção com 'r' (raw string) - mais fácil
downloads = r"D:\Downloads"
sites = r"D:\Sites"
onedrive = r"C:\Users\Caio\OneDrive"
filezilla = r"D:\Program Files\FileZilla FTP Client\filezilla.exe"

firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"

os.startfile(downloads)
os.startfile(sites)
os.startfile(firefox)
os.startfile(onedrive)
os.startfile(filezilla)
webbrowser.open("https://web.whatsapp.com/")
webbrowser.open("https://calendar.google.com/calendar/render?tab=wc&pli=1#main_7")

time.sleep(30)

webbrowser.open("http://localhost/")