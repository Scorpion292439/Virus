import os, sys, time, threading, random, json
from colorama import Fore, Style, init
init(autoreset=True)

R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT

# Token sistemi (kaldırılamaz – Firebase'den kontrol)
def check_token(token):
    try:
        import requests
        r = requests.get("https://ipchecer-default-rtdb.firebaseio.com/tokens.json", timeout=10)
        for x in r.json().values():
            if str(x.get("token")).strip() == token.strip():
                return True
        return False
    except:
        return False

# Login (bypass edilemez)
os.system("clear" if os.name == "posix" else "cls")
print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║              SCORPION TOOLKIT – GITHUB REPO TOOL BİRLEŞTİRİCİ                ║
║                         Virus Repo'dan Yükleniyor...                          ║
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")

while True:
    token = input(f"{C}Token: {G}").strip()
    if check_token(token):
        print(f"{G}Giriş başarılı! Repo tool'ları yükleniyor...")
        time.sleep(2)
        break
    else:
        print(f"{R}Yanlış token!{W}")

# Otomatik diğer .py'leri import et (Virus klasöründen)
try:
    from PUBGChecker import pubg_main  # PUBG Checker
    from Roblox_V7Tool1 import roblox_main  # Roblox Tool
    from SMSBOMBER import sms_bomber_main  # SMS Bomber
    from Smsyonay_comChecker import smsyonay_main  # Smsyonay Checker
    from Vavsms_comChecker import vavsms_main  # Vavsms Checker
    from instahit import insta_hit_main  # Instagram Hit
    print(f"{G}Tüm tool'lar yüklendi!{W}")
except ImportError as e:
    print(f"{R}Hata: {e} – Dosyaları kontrol et!{W}")
    sys.exit()

# Ana menü (alt alta)
def menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                        SCORPION TOOLKIT v1.0 – REPO BİRLEŞTİRME              ║
{Y}  1 → PUBG Checker             ← PUBGChecker.py
{Y}  2 → Roblox Tool              ← Roblox_V7Tool1.py
{Y}  3 → SMS Bomber               ← SMSBOMBER.py
{Y}  4 → Smsyonay Checker         ← Smsyonay.comChecker.py
{Y}  5 → Vavsms Checker           ← Vavsms.comChecker.py
{Y}  6 → Instagram Hit            ← instahit.py
{Y}  7 → Çıkış
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")
        sec = input(f"{C}Seçim → {G}")
        if sec == "1": pubg_main()
        elif sec == "2": roblox_main()
        elif sec == "3": sms_bomber_main()
        elif sec == "4": smsyonay_main()
        elif sec == "5": vavsms_main()
        elif sec == "6": insta_hit_main()
        elif sec == "7": print(f"{R}Görüşürüz kral! Repo senin...{W}"); sys.exit()
        else: print(f"{R}Geçersiz!{W}"); time.sleep(1)

menu()