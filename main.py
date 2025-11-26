import os
import sys
import time
import importlib.util
from colorama import Fore, Style, init
init(autoreset=True)

R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT

os.system("clear" if os.name == "posix" else "cls")
print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                   SCORPION TOOLKIT – REPO'DAN ÇALIŞIYOR                     ║
║                         Virus Repo Aktif – %100 ÇALIŞIR                      ║
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")

# Token (kaldırılamaz – Firebase)
import requests
def check_token(t):
    try:
        r = requests.get("https://ipchecer-default-rtdb.firebaseio.com/tokens.json", timeout=10)
        return any(str(x.get("token","")).strip() == t.strip() for x in r.json().values())
    except: return False

while True:
    token = input(f"{C}Token: {G}").strip()
    if check_token(token):
        print(f"{G}Giriş başarılı! Tool'lar yükleniyor...{W}")
        time.sleep(2)
        break
    else:
        print(f"{R}Token yanlış!{W}")

# Dosyaları dinamik yükle (büyük/küçük harf fark etmez, hata vermez)
tools = {}

files = {
    "PUBGChecker.py": "pubg",
    "Roblox_V7Tool1.py": "roblox", 
    "SMSBOMBER.py": "smsbomber",
    "Smsyonay.comChecker.py": "smsyonay",
    "Vavsms.comChecker.py": "vavsms",
    "instahit.py": "instahit"
}

for filename, name in files.items():
    if os.path.exists(filename):
        try:
            spec = importlib.util.spec_from_file_location(name, filename)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            tools[name] = module
            print(f"{G}[+] {filename} yüklendi")
        except Exception as e:
            print(f"{R}[-] {filename} yüklenemedi → {e}")
    else:
        print(f"{Y}[-] {filename} bulunamadı!")

time.sleep(2)

# Ana Menü
while True:
    os.system("clear" if os.name == "posix" else "cls")
    print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                          SCORPION TOOLKIT – REPO V1                          ║
{Y}  1 → PUBG Checker
{Y}  2 → Roblox Tool
{Y}  3 → SMS Bomber
{Y}  4 → Smsyonay.com Checker
{Y}  5 → Vavsms.com Checker
{Y}  6 → Instagram Hit
{Y}  7 → Çıkış
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")
    sec = input(f"{C}Seçim → {G}")

    if sec == "1" and "pubg" in tools:
        try: tools["pubg"].main()
        except: tools["pubg"].start()
    elif sec == "2" and "roblox" in tools:
        try: tools["roblox"].main()
        except: tools["roblox"].start()
    elif sec == "3" and "smsbomber" in tools:
        try: tools["smsbomber"].main()
        except: tools["smsbomber"].start()
    elif sec == "4" and "smsyonay" in tools:
        try: tools["smsyonay"].main()
        except: tools["smsyonay"].start()
    elif sec == "5" and "vavsms" in tools:
        try: tools["vavsms"].main()
        except: tools["vavsms"].start()
    elif sec == "6" and "instahit" in tools:
        try: tools["instahit"].main()
        except: tools["instahit"].start()
    elif sec == "7":
        print(f"{R}Görüşürüz kral! Repo senin hakimiyetinde...{W}")
        sys.exit()
    else:
        print(f"{R}Seçim hatalı veya dosya eksik!{W}")
        time.sleep(2)
