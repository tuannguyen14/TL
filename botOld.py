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

os.system('cls||clear')

emailObjectNumber = {
  "1": "tuannguyen7067", #11 
  "2": "tuan147067", #13
  "3": "nguyenductuan10a4", #14
  "4": "tuaansnguyeenx95",
  "5": "tuannguyen147067",
  "6": "tuannguyen807067",
  "7": "jsontn1995",
  "8": "pocollo1596",
  "9": "pocollo369",
  "10": "pocollo789",
  "11": "pocollo147",
  "12": "pocollo012",
  "13": "pocollo234",
  "14": "nhungto12xt",
  "15": "nhung.to.leo1996",
  "16": "lunalight067",
  "17": "shadowshaman494",
  "18": "tuannhung1467",
  "19": "minhlum192929",
  "20": "minhanhlom193838",
  "21": "zanglam192929",
  "21": "hungtri6996",
  "22": "linhnhi31627",
  "23": "lydoicoi5863",
  "24": "phuonghoai26253",
  "25": "namphong36152",
  "26": "longtham5965",
  "27": "quanlong4968",
}

arrayEmail = ["tuannguyen7067", "tuan147067", "nguyenductuan10a4", "tuaansnguyeenx95", "tuannguyen147067", "tuannguyen807067",  "jsontn1995", "pocollo1596", "pocollo369", "pocollo789", "pocollo147", "pocollo012", "pocollo234", "nhungto12xt", "nhung.to.leo1996"]

print(colored("     Creator: TuanNguyen     ", "yellow", "on_green"))
print(colored(json.dumps(arrayEmail, indent=4, sort_keys=False), "magenta"))
print("Nhập email bằng số thứ tự: ")
number = int(input())
email = emailObjectNumber[str(number)]
email = emailObjectNumber[str(number)] + '@gmail.com'
password = "AdMiN123"

gameData = None
accessToken = "eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2MzQwMjgxNDM2YjNjMWQ1OGYxZDM1ZWEiLCJyb2xlIjpudWxsLCJpYXQiOjE2NjU0NzU3OTgsImV4cCI6MTY5NjU3OTc5OH0.80b7EaTiCgqXaN3yPU05pdB_NV4ixNOd-vyisBK69-XkUeGGWwDwNbSBOT27pD1bVaCyON2cvL0CMEd3E5OYyQ"
timer = 1

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
    headers["Host"] = "game-api.tl.games"
    headers["Connection"] = "keep-alive"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "*/*"
    headers["Origin"] = "app://"
    headers["Sec-Fetch-Site"] = "cross-site"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Accept-Language"] = "en-US"
    headers["Accept-Encoding"] = "gzip, deflate"

    data = {
        "email": email,
        "password": password
    }

    onPrint("Current login data: ", "yellow")
    onPrint("   UserName: " + email, "green")
    onPrint("   Passwors: " + password, "green")

    time.sleep(1)

    onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    loginResult = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Đăng nhập ngon lành lun!", "green")
        onPrint(loginResult, "green")
        global accessToken
        accessToken = loginResult['accessToken']
        onStartGame()
        
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)

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

    loading(3)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Start game success!", "green")
        onPrint(result, "green")
        global gameData
        gameData = result
    else:
        onPrint("   Start game failed!", "red")
        print(result)

def onPlayingGame():
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

    loading(150)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Update balance game success!", "green")
        onPrint(result, "green")
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

    loading(1)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Update time success!", "green")
        onPrint(result, "green")
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

    loading(3)

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

      "Point:20; Monster:0; ClickCount:0; KillTime:100; isBoss:true",
      
      "Skill Id: 1 Combo",
      "Skill Id: 2 Crippling Strike",
      "Skill Id: 3 Weakness",
      "Skill Id: 4 Battle trance",
      "Skill Id: 5 Vulnerability",
      "Skill Id: 10 Elemental disbalance",
      "Skill Id: 9 Cold Rush",
      "Skill Id: 6 Flaming Blade",
      "Skill Id: 7 Acid Burn",
      "Skill Id: 8 Flesh Erosion",
      "Skill Id: 11 Open Wounds",
      "Skill Id: 12 Sucker Punch",
      "Skill Id: 13 Wildfire",
      "Skill Id: 14 Vampirism",
      "Skill Id: 15 Tranquility",
      "Skill Id: 17 Soul prism",
      "Skill Id: 16 Enchanted Weapon",
      "Skill Id: 18 Inner Fire",
      "Skill Id: 21 Accumulation",
      "Skill Id: 22 Ionization",
      "Skill Id: 23 Arms lore",
      "Skill Id: 24 Fencing",
      "Skill Id: 25 Critical strike",
      "Skill Id: 26 Perfect Vessel",
      "Skill Id: 27 Harmony",
      "Skill Id: 19 Electric charge",
      "Skill Id: 20 Lightning burst"
   ]
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Get Stat game success!", "green")
        onPrint(result, "green")
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
        while (True):
            onLogin()
            if (gameData != None):
                for i in range(0, 20):
                    if i % 2 == 0 and i >= 2:
                        onUpdateTime()
                    time.sleep(randint(1, 7))
                    onPlayingGame()
            onGetStatGame()
            onEndGame()
    except Exception as e:
        onPrint(e, 'red')

main()