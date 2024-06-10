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


    # "21": "zanglam192929",
emailObjectNumber = {}

with open('emails.json', 'r') as openfile:
    emailObjectNumber = json.load(openfile)


skills =   ["Skill Id: 1 Combo", "Skill Id: 2 Crippling Strike", "Skill Id: 3 Weakness", "Skill Id: 4 Battle trance", "Skill Id: 5 Vulnerability", "Skill Id: 10 Elemental disbalance", "Skill Id: 9 Cold Rush", "Skill Id: 6 Flaming Blade", "Skill Id: 7 Acid Burn", "Skill Id: 8 Flesh Erosion","Skill Id: 11 Open Wounds","Skill Id: 12 Sucker Punch","Skill Id: 13 Wildfire", "Skill Id: 14 Vampirism", "Skill Id: 15 Tranquility", "Skill Id: 17 Soul prism", "Skill Id: 16 Enchanted Weapon", "Skill Id: 18 Inner Fire", "Skill Id: 21 Accumulation", "Skill Id: 22 Ionization", "Skill Id: 23 Arms lore", "Skill Id: 24 Fencing", "Skill Id: 25 Critical strike", "Skill Id: 26 Perfect Vessel", "Skill Id: 27 Harmony", "Skill Id: 19 Electric charge", "Skill Id: 20 Lightning burst"]
shuffle(skills)

number = ""
email = ""
password = "AdMiN123"

gameData = None
accessToken = ""
maintoken = ""
timer = 1

print(colored(number, "yellow"))

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
    onPrint(email, "green")
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


######################################################################################################################################################
def onCheckGameEquiptedItem():
    url = "https://game-api.tl.games/game-inventory/equipments?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    # onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        result = result['equipments']
        for item in result:
            onPrint("   Đồ đang mặc!", "green")
            print(item['_id'])
        return result
    else:
        onPrint("   Login failed!", "red")
        print(result)

def onCheckGameFreeItem(itemType):
    url = "https://game-api.tl.games/game-inventory/items?authToken=" + accessToken + "&itemType=" + itemType

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return result['items'][0]['_id']
    else:
        onPrint("   Login failed!", "red")
        print(result)

def onGetGameInventory():
    url = "https://game-api.tl.games/game-inventory/equipments?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    # onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return result
    else:
        onPrint("   Login failed!", "red")
        print(result)

def onEquipEquipment(id):
    url = "https://game-api.tl.games/game-inventory/equip?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    time.sleep(1)

    data = {
        "itemId" : id
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Mặc đồ thanh cong", 'green')
        print(result)
    else:
        onPrint("   Mặc đồ failed!", "red")
        print(result)

def onUnequipEquipment(id):
    url = "https://game-api.tl.games/game-inventory/unequip?authToken="  + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    time.sleep(1)

    data = {
        "itemId" : id
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        print(result)
        onPrint("   Tháo đồ thanh cong", 'green')
    else:
        onPrint("   Tháo đồ failed!", "red")
        print(result)

def onGetLastLobby():
    url = "https://game-api.tl.games/clicker/currentLobbyInfo?authToken=" + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return result
    else:
        onPrint("   Get Last Lobby failed!", "red")
        print(result)

def onCancelLastLobby(id):
    url = "https://game-api.tl.games/clicker/lobby/cancel?authToken="  + accessToken

    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    headers["User-Agent"] = "TLClicker/++UE5+Release-5.0-CL-20979098 Windows/10.0.22000.1.768.64bit"

    data = {
        "lobbyId" : id
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        print(result)
        onPrint("   Cancel Last Lobby success!", "green")
    else:
        onPrint("   Cancel Last Lobby failed!", "red")
        print(result)
######################################################################################################################################################

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
        ]
    }

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Cancel item success!", "green")
        return result   
    else:
        onPrint("   Cancel item failed!", "red")
        print(result)

def onGetMainListItem():
    url = "https://game-api.tl.games/rent/manage/list"

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

    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        onPrint("   Cancel item success!", "green")
        return result   
    else:
        onPrint("   Cancel item failed!", "red")
        print(result)

def main():
    try:
        # onLoginMain()

        number = int(input())
        global email
        email = emailObjectNumber[str(number)] + '@gmail.com'
        
        onLogin()
        # onRentItem('633ffc95a438b92bb6450659')

        lastLobby = onGetLastLobby()
        print(lastLobby["lobbyId"])
        if lastLobby["lobbyId"] != None:
            onCancelLastLobby(lastLobby["lobbyId"])

        time.sleep(3)
        equiptedItems = onCheckGameEquiptedItem()
        if len(equiptedItems) > 0:
            #Tháo đồ ra
            for item in equiptedItems:
                onUnequipEquipment(item['_id'])

        itemTypes = ['armor', 'sword']
        armor = onCheckGameFreeItem(itemTypes[0])
        sword = onCheckGameFreeItem(itemTypes[1])

        onEquipEquipment(armor)
        onEquipEquipment(sword)
        
    except Exception as e:
        onPrint(e, 'red')
        loading(78)
        main()
        
main()