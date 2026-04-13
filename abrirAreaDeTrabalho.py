import os

# Opção com 'r' (raw string) - mais fácil
downloads = r"D:\Downloads"
sites = r"D:\Sites"
onedrive = r"C:\Users\Caio\OneDrive"
filezilla = r"D:\Program Files\FileZilla FTP Client\filezilla.exe"

firefox = r"C:\Program Files\Mozilla Firefox\firefox.exe"
acessarWhatsAppPeloFirefox = r"C:\Program Files\Mozilla Firefox\firefox.exe https://web.whatsapp.com/"
acessarAgendaPeloFirefox = r"C:\Program Files\Mozilla Firefox\firefox.exe https://calendar.google.com/calendar/u/0/r"

os.startfile(downloads)
os.startfile(sites)
os.startfile(firefox)
os.startfile(onedrive)
os.startfile(filezilla)
os.startfile(acessarWhatsAppPeloFirefox)
os.startfile(acessarAgendaPeloFirefox)