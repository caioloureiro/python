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

print("Abrindo pastas Downloads...")
os.startfile(downloads)

print("Abrindo pastas Sites...")
os.startfile(sites)
print("Abrindo pastas OneDrive...")
os.startfile(onedrive)
print("Abrindo FileZilla...")
os.startfile(filezilla)
print("Abrindo Firefox...")
os.startfile(firefox)

print("Aguardando 2 segundos WhatsApp...")
time.sleep(2)

webbrowser.open("https://web.whatsapp.com/")

print("Aguardando 2 segundos Google Calendar...")
time.sleep(2)

webbrowser.open("https://calendar.google.com/calendar/render?tab=wc&pli=1#main_7")

print("Aguardando 2 segundos localhost...")
time.sleep(2)

webbrowser.open("http://localhost/")