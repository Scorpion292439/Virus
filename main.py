import os
import sys
import time
import importlib.util
import requests
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
║                   SCORPION TOOLKIT – REPO TOOL BİRLEŞTİRİCİ v1.0             ║
║                         Dosyalar Yükleniyor...                               ║
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")

# Token sistemi (kaldırılamaz)
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

# Dosya isimlerini tam olarak tanımla (senin verdiğin gibi)
tool_files = {
    "PUBGChecker.py": "PUBG Checker",
    "Roblox_V7Tool1.py": "Roblox Tool",
    "SMSBOMBER.py": "SMS Bomber",
    "Smsyonay.comChecker.py": "Smsyonay Checker",
    "Vavsms.comChecker.py": "Vavsms Checker",
    "instahit.py": "Instagram Hit"
}

tools = {}
for filename, display_name in tool_files.items():
    if os.path.exists(filename):
        try:
            # Dosyayı oku ve exec ile çalıştır (modül adı sorununu atlar)
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
            # Yeni namespace'te çalıştır
            namespace = {}
            exec(code, namespace)
            tools[display_name] = namespace
            print(f"{G}[+] {filename} yüklendi ({display_name})")
        except Exception as e:
            print(f"{R}[-] {filename} yüklenemedi → {e}")
    else:
        print(f"{Y}[-] {filename} bulunamadı!")

time.sleep(2)

# Ana Menü (alt alta)
def menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                          SCORPION TOOLKIT – REPO v1.0                        ║
{Y}  1 → PUBG Checker              ← PUBGChecker.py
{Y}  2 → Roblox Tool               ← Roblox_V7Tool1.py
{Y}  3 → SMS Bomber                ← SMSBOMBER.py
{Y}  4 → Smsyonay Checker          ← Smsyonay.comChecker.py
{Y}  5 → Vavsms Checker            ← Vavsms.comChecker.py
{Y}  6 → Instagram Hit             ← instahit.py
{Y}  7 → Çıkış
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")
        sec = input(f"{C}Seçim → {G}")
        if sec == "1":
            if "PUBG Checker" in tools:
                try:
                    tools["PUBG Checker"].main() if "main" in tools["PUBG Checker"] else tools["PUBG Checker"].start()
                except Exception as e:
                    print(f"{R}PUBG Checker çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}PUBGChecker.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "2":
            if "Roblox Tool" in tools:
                try:
                    tools["Roblox Tool"].main() if "main" in tools["Roblox Tool"] else tools["Roblox Tool"].start()
                except Exception as e:
                    print(f"{R}Roblox Tool çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}Roblox_V7Tool1.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "3":
            if "SMS Bomber" in tools:
                try:
                    tools["SMS Bomber"].main() if "main" in tools["SMS Bomber"] else tools["SMS Bomber"].start()
                except Exception as e:
                    print(f"{R}SMS Bomber çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}SMSBOMBER.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "4":
            if "Smsyonay Checker" in tools:
                try:
                    tools["Smsyonay Checker"].main() if "main" in tools["Smsyonay Checker"] else tools["Smsyonay Checker"].start()
                except Exception as e:
                    print(f"{R}Smsyonay Checker çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}Smsyonay.comChecker.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "5":
            if "Vavsms Checker" in tools:
                try:
                    tools["Vavsms Checker"].main() if "main" in tools["Vavsms Checker"] else tools["Vavsms Checker"].start()
                except Exception as e:
                    print(f"{R}Vavsms Checker çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}Vavsms.comChecker.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "6":
            if "Instagram Hit" in tools:
                try:
                    tools["Instagram Hit"].main() if "main" in tools["Instagram Hit"] else tools["Instagram Hit"].start()
                except Exception as e:
                    print(f"{R}Instagram Hit çalıştırılamadı → {e}{W}")
                    input("Enter...")
            else:
                print(f"{R}instahit.py bulunamadı!{W}")
                input("Enter...")
        elif sec == "7":
            print(f"{R}Görüşürüz kral! Repo hakimiyetinde...{W}")
            sys.exit()
        else:
            print(f"{R}Geçersiz seçim!{W}")
            time.sleep(1)

menu()
