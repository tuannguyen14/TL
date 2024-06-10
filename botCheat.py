import requests
from requests.structures import CaseInsensitiveDict
import json
import string
import random
from termcolor import colored
import os
import time
from random import randint, shuffle
from tqdm import tqdm
import math
import urllib.request

os.system('cls||clear')

skills =   ["Skill Id: 1 Combo", "Skill Id: 2 Crippling Strike", "Skill Id: 3 Weakness", "Skill Id: 4 Battle trance", "Skill Id: 5 Vulnerability", "Skill Id: 10 Elemental disbalance", "Skill Id: 9 Cold Rush", "Skill Id: 6 Flaming Blade", "Skill Id: 7 Acid Burn", "Skill Id: 8 Flesh Erosion","Skill Id: 11 Open Wounds","Skill Id: 12 Sucker Punch","Skill Id: 13 Wildfire", "Skill Id: 14 Vampirism", "Skill Id: 15 Tranquility", "Skill Id: 17 Soul prism", "Skill Id: 16 Enchanted Weapon", "Skill Id: 18 Inner Fire", "Skill Id: 21 Accumulation", "Skill Id: 22 Ionization", "Skill Id: 23 Arms lore", "Skill Id: 24 Fencing", "Skill Id: 25 Critical strike", "Skill Id: 26 Perfect Vessel", "Skill Id: 27 Harmony", "Skill Id: 19 Electric charge", "Skill Id: 20 Lightning burst"]
shuffle(skills)

maintoken = ""

emailObjectNumber = {
}

with open('emails.json', 'r') as openfile:
    emailObjectNumber = json.load(openfile)

number = ""
email = ""
password = "AdMiN123"

gameData = None
accessToken = ""
timer = 1

cancelItemsList = []

def isConnect(host='http://google.com'):
    try:
        urllib.request.urlopen(host) #Python 3.x
        return True
    except:
        return False

def onPrint(text, color):
  print(colored(" " + str(text), color))

def loading(timeLoop):
  timeLoop = math.floor(timeLoop)
  for i in tqdm(range(timeLoop)):
    time.sleep(1)

def onLogin():
    url = "https://game-api.tl.games/auth/login"

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
        "email": email,
        "password": password
    }

    onPrint("Current login data: ", "yellow")
    onPrint("   UserName: " + email, "green")

    time.sleep(1)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    loginResult = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        global accessToken
        accessToken = loginResult['accessToken']
        
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)

def onLoginMain():
    url = "https://game-api.tl.games/auth/login"

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
        "email": 'tuannguyen7067@gmail.com',
        "password": password
    }

    time.sleep(1)

    # onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    loginResult = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        global maintoken
        maintoken = loginResult['accessToken']
        
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)


def onRentItem(id):
    url = "https://game-api.tl.games/rent/apply"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Authorization"] = accessToken
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
        "lotId": id
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint(result, "green")
    else:
        onPrint("   Rent item failed!", "red")
        print(result)

def onCheckEquipment():
    url = "https://game-api.tl.games/game-inventory/equipments?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"

    time.sleep(1)

    # onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.get(url, headers=headers)
    loginResult = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return loginResult
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)

def onEquipEquipment(id):
    url = "https://game-api.tl.games/game-inventory/equip?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"

    time.sleep(1)

    data = {
        "itemId" : id
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    loginResult = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Mac do thanh cong", 'green')
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)

def onCreateItem(id):
    url = "https://game-api.tl.games/rent/manage/create"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Authorization"] = maintoken
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
        "items": [
            id
        ],
        "rentalTime": 86400,
        "tax": 50
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Create item success!", "green")
        return result   
    else:
        onPrint("   Create item failed!", "red")
        print(result)

def onCancelItem(id):
    url = "https://game-api.tl.games/rent/manage/cancel"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Authorization"] = maintoken
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
        "lotIds": [
            id
        ],
        "rentalTime": 86400,
        "tax": 50
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Cancel item success!", "green")
        return result   
    else:
        onPrint("   Cancel item failed!", "red")
        print(result)

def onGetListRentItems():
    url = "https://game-api.tl.games/rent/list?page=2"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "en-US,en;q=0.9"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["Origin"] = "https://market.tl.games"
    headers["Pragma"] = "no-cache"
    headers["Referer"] = "https://market.tl.games/"
    headers["Sec-Ch-Ua"] = "Chromium;v=106, Google Chrome;v=106, Not;A=Brand;v=99"
    headers["Sec-Ch-Ua-Mobile"] = "?0"
    headers["Sec-Ch-Ua-Platform"] = "Windows"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-site"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"

    loading(3)

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)
    print(result)
    if (respLogin.status_code == 200):
        return result['balances']['crystal']
    else:
        onPrint("   Start game failed!", "red")
        print(result)

def onStartGame():
    url = "https://game-api.tl.games/game/start?auto=0"

    headers = CaseInsensitiveDict()
    headers["Host"] = "game-api.tl.games"
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
    headers["Accept-Encoding"] = "gzip, deflate"

    data = {
        "mine" : "common",
        "authToken" : accessToken
    }

    time.sleep(1)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        global gameData
        gameData = result
    else:
        onPrint("   Start game failed!", "red")
        print(result)

def onPlayingGame(i):
    url = "https://game-api.tl.games/game-account/gold-balance"

    headers = CaseInsensitiveDict()
    headers["Host"] = "game-api.tl.games"
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
    headers["Accept-Encoding"] = "gzip, deflate"

    data = {
        "authToken" : accessToken,
        "goldBalance" : randint(1, 17),
        "operation" : "increase"
    }

    # os.system('cls||clear')

    onPrint(number, 'yellow')
    onPrint(email, 'green')

    if (i <= 12 ):
        loading(100)
    else:
        loading(150)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        time.sleep(1)
    else:
        onPrint("   Update balance game failed!", "red")
        print(result)

def onUpdateTime():
    url = "https://game-api.tl.games/clicker/lobby/timeSpent?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    headers["Host"] = "game-api.tl.games"
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
    headers["Accept-Encoding"] = "gzip, deflate"

    data = {
        "lobbyId" : gameData['lobbyId'],
        "time" : 300
    }

    time.sleep(1)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        time.sleep(1)
    else:
        onPrint("   Update time failed!", "red")
        print(result)


def onGetStatGame():
    url = "https://game-api.tl.games/game/stats"

    headers = CaseInsensitiveDict()
    headers["Host"] = "game-api.tl.games"
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
    headers["Accept-Encoding"] = "gzip, deflate"

    time.sleep(3)

    data = {
        "lobbyId" : gameData['lobbyId'],
        "stats" : [
      "Point:1; Monster:1; ClickCount:0; KillTime:" + str(randint(1, 10)) + "; isBoss:false",
      "Point:1; Monster:2; ClickCount:0; KillTime:" + str(randint(1, 10)) + "; isBoss:false",

      "Point:2; Monster:1; ClickCount:0; KillTime:" + str(randint(5, 10)) + "; isBoss:false",
      "Point:2; Monster:2; ClickCount:0; KillTime:" + str(randint(5, 10)) + "; isBoss:false",

      "Point:3; Monster:1; ClickCount:0; KillTime:" + str(randint(10, 15)) + "; isBoss:false",
      "Point:3; Monster:2; ClickCount:0; KillTime:" + str(randint(10, 15)) + "; isBoss:false",

      "Point:4; Monster:1; ClickCount:0; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:2; ClickCount:0; KillTime:" + str(randint(15, 20)) + "; isBoss:false",
      "Point:4; Monster:3; ClickCount:0; KillTime:" + str(randint(15, 20)) + "; isBoss:false",

      "Point:5; Monster:1; ClickCount:0; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:2; ClickCount:0; KillTime:" + str(randint(20, 25)) + "; isBoss:false",
      "Point:5; Monster:3; ClickCount:0; KillTime:" + str(randint(20, 25)) + "; isBoss:false",

      "Point:6; Monster:1; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:2; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:6; Monster:3; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:7; Monster:1; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:2; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:7; Monster:3; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:8; Monster:1; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:8; Monster:2; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:8; Monster:3; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:9; Monster:1; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:9; Monster:2; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:9; Monster:3; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      
      "Point:10; Monster:1; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:2; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:3; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",
      "Point:10; Monster:4; ClickCount:0; KillTime:" + str(randint(25, 30)) + "; isBoss:false",

      "Point:11; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:11; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:11; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:11; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:12; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:12; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:12; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:12; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:12; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:13; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:13; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      
      "Point:14; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:14; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:15; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:15; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:16; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:16; Monster:8; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:17; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:8; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:9; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:10; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:11; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:12; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:17; Monster:13; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:18; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:8; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:9; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:10; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:11; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:12; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:13; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:18; Monster:14; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:19; Monster:1; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:2; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:3; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:4; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:5; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:6; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:7; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:8; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:9; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:10; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:11; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:12; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:13; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:14; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",
      "Point:19; Monster:15; ClickCount:0; KillTime:" + str(randint(50, 55)) + "; isBoss:false",

      "Point:20; Monster:0; ClickCount:0; KillTime:" + str(randint(50, 100)) + "; isBoss:true",
      
      skills[0],
      skills[1],
      skills[2],
      skills[3],
      skills[4],
      skills[5],
      skills[6],
      skills[7],
      skills[8],
      skills[9],
      skills[10],
      skills[11],
      skills[12],
      skills[13],
      skills[14],
      skills[15],
      skills[16],
      skills[17],
      skills[18],
      skills[19],
      skills[20],
      skills[21],
      skills[22],
      skills[23],
      skills[24],
      skills[25],
      skills[26]
   ]
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        time.sleep(1)
    else:
        onPrint("   Get Stat game failed!", "red")
        print(result)


def onEndGame():
    url = "https://game-api.tl.games/game/end"

    headers = CaseInsensitiveDict()
    headers["Host"] = "game-api.tl.games"
    headers["Accept"] = "*/*"
    headers["Content-Type"] = "application/json"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"
    headers["Accept-Encoding"] = "gzip, deflate"

    data = {
        "lobbyId" : gameData['lobbyId'],
        "result" : "true",
        "secretKey" : gameData['secretKey']
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   End game success!", "green")
        onPrint(result, "green")
    else:
        onPrint("   End game failed!", "red")
        print(result)


def main():
    try:
        print("Nhập email bằng số thứ tự: ")
        print(colored(json.dumps(emailObjectNumber, indent=4, sort_keys=False), "magenta"))
        global number
        number = int(input())
        global email
        email = emailObjectNumber[str(number)] + '@gmail.com'
        onLoginMain()
        while (True):
            os.system('cls||clear')
            if (number > 1):
                onLogin()
                cancelItemsList = []
                    #create
                item = onCreateItem('634d5d8ad5059d392000cdbb')
                cancelItemsList.append(item['rentIds'][0])
                item = onCreateItem('634ce46236b3c1d58f3155a6')
                cancelItemsList.append(item['rentIds'][0])
                print(cancelItemsList)

                    #onRentItem
                onRentItem(cancelItemsList[0])
                onRentItem(cancelItemsList[1])

                    #equip
                equipments = onCheckEquipment()
                # print(equipments)
                if (len(equipments['equipments']) == 0):
                    onEquipEquipment('634d5d8ad5059d392000cdbb')
                    onEquipEquipment('634ce46236b3c1d58f3155a6')

                    #StartGame
                onStartGame()

                    #cancel
                item = onCancelItem(cancelItemsList[0])
                item = onCancelItem(cancelItemsList[1])
                cancelItemsList = []

                if (gameData != None):
                    for i in range(0, 20):
                        if i % 3 == 0 and i >= 3 and i <= 12:
                            onUpdateTime()
                        elif i % 2 == 0 and i > 12:
                            onUpdateTime()
                        time.sleep(randint(1, 7))
                        onPlayingGame(i)
                        onGetStatGame()
                        onEndGame()
            else:
                onStartGame()
                if (gameData != None):
                    for i in range(0, 20):
                        if i % 3 == 0 and i >= 3 and i <= 12:
                            onUpdateTime()
                        elif i % 2 == 0 and i > 12:
                            onUpdateTime()
                        time.sleep(randint(1, 7))
                        onPlayingGame(i)
                        onGetStatGame()
                        onEndGame()

    except Exception as e:
        onPrint(e, 'red')
        loading(78)
        main()

main()