import os
import webbrowser
import time

print("Abrindo área de trabalho...")
print("Esperar os drivers e o WAMP64 ligarem...")
print("Aguardando 30 segundos...")

time.sleep(30)

# Opção com 'r' (raw string) - mais fácil
downloads = r"D:\Downloads"
sites = r"D:\Sites"
onedrive = r"C:\Users\Caio\OneDrive"
filezilla = r"D:\Program Files\FileZilla FTP Client\filezilla.exe"
firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"

os.startfile(downloads)
os.startfile(sites)
os.startfile(onedrive)
os.startfile(filezilla)
os.startfile(firefox)

webbrowser.open("https://web.whatsapp.com/")
webbrowser.open("https://calendar.google.com/calendar/render?tab=wc&pli=1#main_7")
webbrowser.open("http://localhost/")