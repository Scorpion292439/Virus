import os
import sys
import time
import requests
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# Renk kodları
R = Fore.RED + Style.BRIGHT
G = Fore.GREEN + Style.BRIGHT
Y = Fore.YELLOW + Style.BRIGHT
C = Fore.CYAN + Style.BRIGHT
W = Fore.WHITE + Style.BRIGHT

# Konsolu temizle
os.system("clear" if os.name == "posix" else "cls")

# Başlık
print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                   SCORPION TOOLKIT – REPO TOOL BAŞLATICI v2.0                 ║
║                            Token Kontrolü...                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")

# --- Token Kontrol Sistemi (Verdiğiniz Koddan Alınmıştır) ---
def check_token(t):
    try:
        # Bu URL'nin gerçekten aktif bir Firebase veritabanı olduğunu varsayıyoruz
        r = requests.get("https://ipchecer-default-rtdb.firebaseio.com/tokens.json", timeout=10)
        
        # Eğer yanıt bir sözlük değilse, tokenleri döngüleyerek kontrol et
        data = r.json()
        if isinstance(data, dict):
            return any(str(x.get("token","")).strip() == t.strip() for x in data.values())
        return False
    except requests.exceptions.RequestException: 
        print(f"{R}Bağlantı hatası! Token kontrolü yapılamıyor...{W}")
        return False
    except Exception as e:
        print(f"{R}Token kontrolünde beklenmedik hata: {e}{W}")
        return False


# Token girişi ve kontrolü
while True:
    token = input(f"{C}Token: {G}").strip()
    if check_token(token):
        print(f"{G}Giriş başarılı! Tool'lar yükleniyor...{W}")
        time.sleep(1)
        break
    else:
        print(f"{R}Token yanlış veya bağlantı hatası!{W}")

# --- Tool Yükleme ve Menü Hazırlığı ---

# GitHub görüntüsündeki dosya adları ile menüde görünmesini istediğin adları eşleştir
tool_files = {
    "pubgchecker.py": "PUBG Checker", # pubgchecker.py olarak yeniden adlandırılmış
    "Roblox_V7Tool1.py": "Roblox Tool", # Verdiğin kodda bu ad kullanılmış
    "SMSBOMBER.py": "SMS Bomber",
    "Smsyonay.comChecker.py": "Smsyonay Checker",
    "Vavsms.comChecker.py": "Vavsms Checker",
    "instahit.py": "Instagram Hit"
}

# 'exec' yerine 'os.system' kullanarak dosyayı yeni bir işlemde çalıştırma
# Bu, tool'un kendi başına çalışmasını sağlar ve modül karmaşasını önler.
def run_tool(filename):
    if not os.path.exists(filename):
        print(f"{R}Hata: {filename} dosyası bulunamadı!{W}")
        input("Devam etmek için Enter tuşuna basın...")
        return
        
    print(f"{C}{filename} çalıştırılıyor...{W}")
    # Python dosyasını ayrı bir komut olarak çalıştır
    if sys.platform.startswith('win'):
        os.system(f"python {filename}")
    else:
        os.system(f"python3 {filename}")
        
    input("\nTool çalışması bitti. Menüye dönmek için Enter tuşuna basın...")

# Ana Menü
def menu():
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print(f"""{R}
╔══════════════════════════════════════════════════════════════════════════════╗
║                          SCORPION TOOLKIT – REPO v2.0                        ║
{Y}  1 → PUBG Checker              ← pubgchecker.py
{Y}  2 → Roblox Tool               ← Roblox_V7Tool1.py
{Y}  3 → SMS Bomber                ← SMSBOMBER.py
{Y}  4 → Smsyonay Checker          ← Smsyonay.comChecker.py
{Y}  5 → Vavsms Checker            ← Vavsms.comChecker.py
{Y}  6 → Instagram Hit             ← instahit.py
{Y}  7 → Çıkış
╚══════════════════════════════════════════════════════════════════════════════╝{W}""")
        sec = input(f"{C}Seçim → {G}")
        
        selected_tool = None
        
        # Seçime göre dosyayı belirle
        if sec == "1":
            selected_tool = "pubgchecker.py"
        elif sec == "2":
            selected_tool = "Roblox_V7Tool1.py"
        elif sec == "3":
            selected_tool = "SMSBOMBER.py"
        elif sec == "4":
            selected_tool = "Smsyonay.comChecker.py"
        elif sec == "5":
            selected_tool = "Vavsms.comChecker.py"
        elif sec == "6":
            selected_tool = "instahit.py"
        elif sec == "7":
            print(f"{R}Görüşürüz kral! Repo hakimiyetinde...{W}")
            sys.exit()
        else:
            print(f"{R}Geçersiz seçim!{W}")
            time.sleep(1)
            continue

        # Seçilen tool'u çalıştır (eğer geçerli bir tool seçildiyse)
        if selected_tool:
            run_tool(selected_tool)

# Ana menüyü başlat
menu()
