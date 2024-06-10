import requests
from requests.structures import CaseInsensitiveDict
import json
import string
import random
from termcolor import colored
import os
import time
from random import randint
from tqdm import tqdm
import math
import urllib.request
import string
from twocaptcha import TwoCaptcha
import randominfo as ri

os.system('cls||clear')

password = "AdMiN123"

emailObjectNumber = {}

with open('emails.json', 'r') as openfile:
    emailObjectNumber = json.load(openfile)

def random_char(char_num):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(char_num))

def onPrint(text, color):
  print(colored(" " + str(text), color))

def loading(timeLoop):
  timeLoop = math.floor(timeLoop)
  for i in tqdm(range(timeLoop)):
    time.sleep(1)

def toObject(arr):
    rv = {}
    i = 714
    for email in arr:
        rv[str(i)] = email
        i = i + 1
    return rv

def has_special_char(s):
  for c in s:
    if not (c.isalpha() or c.isdigit() or c == ' '):
      return True
  return False

def solveCaptcha():
    onPrint("Dang giai captcha", 'yellow')
    api_key = os.getenv('APIKEY_2CAPTCHA', '9d38018037c3173eb09205630a36aa8e')

    solver = TwoCaptcha(api_key)
    
    try:
        result = solver.recaptcha(
            sitekey='6LdR_hIjAAAAABd5KRyNqE-uK9qX_UIi7i5_lFWu',
            url='https://market.tl.games/')
        return result

    except Exception as e:
        onPrint(e, 'red')

def onRegiser(email):
    url = "https://game-api.tl.games/auth/register"

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["Origin"] = "https://market.tl.games"
    headers["Referer"] = "https://market.tl.games/"
    headers["Sec-Ch-Ua"] = "Chromium;v=106, Google Chrome;v=106, Not;A=Brand;v=99"
    headers["Sec-Ch-Ua-Mobile"] = "?0"
    headers["Sec-Ch-Ua-Platform"] = "Windows"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"
    
    data = {
        "username": email,
        "email": email  + '@yahoo.com',
        "password": email,
        "token": (solveCaptcha())['code'],
        "check": ""
    }

    onPrint("   UserName: " + email, "green")

    loading(randint(1, 10))

    onPrint("Đang đăng ký...", "yellow")

    try:
        respLogin = requests.post(url, headers=headers, data=json.dumps(data))
        loginResult = json.loads(respLogin.content)

        if (respLogin.status_code == 200):
            return loginResult
            
        else:
            onPrint("   Login failed!", "red")
            print(loginResult)
    except:
        onRegiser(email)

class Person:
    def __init__(self) -> None:
        self.first_name = ri.get_first_name()
        self.last_name = ri.get_last_name()
        self.birthdate = ri.get_birthdate()

# def main():
#     try:
#         emailObjectNumber = []
#         emailRegisted = []
#         store = []
#         for i in range(0, 132):
#             person1 = Person()
#             email = None
#             while(True):
#                 email = ri.get_email(person1).lower()
#                 email = email[0:email.index('@')]
#                 if not has_special_char(email) and len(email) > 5:
#                     break
#             emailObjectNumber.append(email)
#         for email in emailObjectNumber:
#             onRegiser(email)
#             emailRegisted.append(email)
#             store = toObject(emailRegisted)
#             with open('email.txt', 'w') as f:
#                 f.writelines(json.dumps(store, indent=4, sort_keys=False))

def onGenerateEmail():
    email = None

    while(True):
        person1 = Person()
        email = ri.get_email(person1).lower()
        email = email[0:email.index('@')]
        if not has_special_char(email) and len(email) > 7 and email:
            break

    for number in emailObjectNumber:
        if emailObjectNumber[number] == email:
            onGenerateEmail()
    return email

def main():
    try:
        emailRegisted = []
        store = []
        for i in range(0, 300):
            email = onGenerateEmail()            
            result = onRegiser(email)
            print(result)
            try:
                if result['accessToken'] != None:
                    onPrint("   Register sucessful!", "green")
                    onPrint(result, "green")
                    emailRegisted.append(email)
                    store = toObject(emailRegisted)
                    with open('email.txt', 'w') as f:
                        f.writelines(json.dumps(store, indent=4, sort_keys=False))
            except:
                continue

        # data = toObject(emailObjectNumber)
        # with open('email.txt', 'w') as f:
        #     f.writelines(json.dumps(data, indent=4, sort_keys=False))
    except Exception as e:
        onPrint(e, 'red')

main()