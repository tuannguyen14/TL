import requests
from requests.structures import CaseInsensitiveDict
import json
import string
# import random
from termcolor import colored
import os
import time
from random import randint, uniform, shuffle
from tqdm import tqdm
import math
import urllib.request
from twocaptcha import TwoCaptcha
import cv2
from os import listdir
import numpy as np
import mss
import pyautogui
import time
import yaml

stream = open("./config.yaml", 'r')
c = yaml.safe_load(stream)
ct = c['threshold']
ch = c['home']
pause = c['time_intervals']['interval_between_moviments']
pyautogui.PAUSE = 0.01
# hc = HumanClicker()
pyautogui.FAILSAFE = False

os.system('cls||clear')

emailObjectNumber = {}

# wallets = ["0xd5e337dB6645C836D27b740E31d86Ab08E80e416", "0xd5e337dB6645C836D27b740E31d86Ab08E80e416", "0xA0C3c0A8B3828E560d2F77095B9c8a7a084f094b", "0xa804AeF665Bd4B9A65F34013bc97CbE26b396268", "0xBA1b9D37206fC4d23E6E4fFB1a9bD34A4C3919Af", "0xD1419CE0E9e7F818c21eaFA9dB30CA0c69C5Ca5a", 
#      "0x2e4C552Db8da0ccc34e0B6B03b45e9ecDF3D4736", "0xe10BefbAd5Ff9CE4f7659DF6E1C957A475195E84", "0x159A2aC8437258b36c758D6D87E2e873B7F35329", "0x091Ba381912266e7eC8f820eBA7B63E4CbBC7210", "0x7D6d205b936688050Bbd5d8A38590F704c218656", 
#      "0x94Bc1752AA5493a1108f3707b91427ce9C46bd2e", "0xDfe93a64e373927A027C8e097EDCd119c5c2B8E1", "0x6086E5f2c0C3aCEEFf81D59A7C705DadBB3789fE", "0xd510e04Db074ce8C38d351735D53b491c2357ffE", "0xd1651e0538A9FadBd305584A963976cB83B98523",
#      "0x4CdfC14161931ab6013f0f896FE1E72bE2aB7faA", "0xA56c00bB9971D0945EB9F6eE8B3893a35Bf36502", "0x07bB88e59f7dbdd134e642E9bf44dDDCFa009B58", "0x7626FDafC86EDf48cC77622b2AcF6AD463b95A6D", "0xF4DD829CB441Fa6b81808540D0Ee4e70c039ccC1", "0x3F85aB6bb358065E3227311763696792a37427e8"]

wallets = [
    "0x18F058f0B80a34D702687bCAFc2C724f034bAc89", "0xB3929CD9a36D5E570236187a82fC6a19CA00dC75", "0x5149E553FF7f1d24038a4012C4422Cf9d93d591e", 
    "0xa4576e42DA726A57Ab8661Fd30f997e15E0Cff33", "0x5f36E438385C427ABd4d9D0559fC1352928e82d4", "0x63d425a90b080B52a9B31422b4BD7FE15b2D2a81", 
    "0x7eCBA285b233e634247Fc296A719b8e49CF3Bd53", "0x1e59491427b6BD8d28C63C04B6C51b7E7Ae5a7F3", "0x799381aB0693f3A10E4Ce4FEae441755B015b206",
    "0x5feE3B96316Ee285eE74D82f67c30768D8267E1a", "0xe160367e3471da96f8A5Ce8C62b4b29724D61dB5", "0xC50AcE3415F81B5e1d3737CfAbC840f62e164D08"]

with open('emails.json', 'r') as openfile:
    emailObjectNumber = json.load(openfile)

# print(colored(json.dumps(emailObjectNumber, indent=4, sort_keys=False), "magenta"))

password = "AdMiN123"

gameData = None
accessToken = ""
timer = 1

images = []

totalDone = 0

headers = []

resultWithdraw = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0,
    "10": 0,
    "11": 0,
    "12": 0,
    "13": 0,
    "14": 0,
    "15": 0,
    "16": 0,
    "17": 0,
    "18": 0,
    "19": 0,
    "20": 0,
    "21": 0
}

def remove_suffix(input_string, suffix):
    """Returns the input_string without the suffix"""

    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

def load_images(dir_path='./targets'):
    file_names = listdir(dir_path)
    targets = {}
    for file in file_names:
        path = 'targets/' + file
        targets[remove_suffix(file, '.png')] = cv2.imread(path)

    return targets


def clickBtn(img, timeout=3, threshold = ct['default']):
    # logger(None, progress_indicator=True)
    start = time.time()
    has_timed_out = False
    while (not has_timed_out):
        matches = positions(img, threshold=threshold)

        if(len(matches)==0):
            has_timed_out = time.time() - start > timeout
            continue

        x,y,w,h = matches[0]
        pos_click_x = x+w/2
        pos_click_y = y+h/2
        pyautogui.moveTo(pos_click_x,pos_click_y,0.3)
        pyautogui.click()
        return True
    return False

def checkTimeOut(timeout):
    start = time.time()
    has_timed_out = False
    while (not has_timed_out):
        has_timed_out = time.time() - start > timeout
        return True
    return False

def printSreen():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = np.array(sct.grab(monitor))
        # The screen part to capture
        # monitor = {"top": 160, "left": 160, "width": 1000, "height": 135}

        # Grab the data
        return sct_img[:,:,:3]

def positions(target, threshold=ct['default'], img = None):
    if img is None:
        img = printSreen()
    result = cv2.matchTemplate(img,target,cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]

    yloc, xloc = np.where(result >= threshold)


    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
    return rectangles

def checkIsButtonExist(img, threshold = ct['default'], timeout=0):
    start = time.time()
    has_timed_out = False
    while (not has_timed_out):
        matches = positions(img, threshold=threshold)

        if (len(matches) == 0):
            has_timed_out = time.time() - start > timeout
            continue
        if (len(matches) > 0):
            return True
    return False

def onIfError():
    pyautogui.press('f5')
    onLogout()

def onTypeEmailPassword(word):
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    for i in range (0, len(word)):
        pyautogui.press(word[i])

def onLoginByBot(email, password):
    clickBtn(images['profile'], 60)
    if (not clickBtn(images['email'], 60)):
        onIfError()
        onLoginByBot(email, password)
    time.sleep(1)
    onTypeEmailPassword(email)
    clickBtn(images['password'], 60)
    time.sleep(1)
    onTypeEmailPassword(password)
    clickBtn(images['login'], 60)
    while (checkIsButtonExist(images['login'], 0.7, 1)):
        time.sleep(1)

def onPutNft():
    clickBtn(images['gaming'], 60, 0.7)
    while (not checkIsButtonExist(images['loading-gaming'], 0.7, 60)):
        pyautogui.press('f5')
        time.sleep(5)
        clickBtn(images['gaming'], 60)
    clickBtn(images['sword'], 60)
    clickBtn(images['confirm'], 60)
    clickBtn(images['details'], 60)
    clickBtn(images['details'], 60)
    while True:
        if checkIsButtonExist(images['confirm-metamask']):
            break
        pyautogui.scroll(-60)
    time.sleep(5)
    while True:
        if checkIsButtonExist(images['reject']):
            break
        pyautogui.scroll(-60)
    pyautogui.scroll(-60)
    pyautogui.scroll(-60)
    clickBtn(images['confirm-metamask'], 60)
    time.sleep(1)

def onLogout():
    clickBtn(images['profile'], 120)
    if not clickBtn(images['logout'], 60):
        pyautogui.press('f5')
        onLogout()
    clickBtn(images['logout'], 1)
    clickBtn(images['logout'], 1)

def onPrint(text, color):
  print(colored(" " + str(text), color))

def loading(timeLoop):
  timeLoop = math.floor(timeLoop)
  for i in tqdm(range(timeLoop)):
    time.sleep(1)

def onLogin(email):
    url = "https://game-api.tl.games/auth/login"
    global headers
    headers = CaseInsensitiveDict()
    
    headers["Accept"] = "*/*"
    headers["Accept-Encoding"] = "gzip, deflate, br"
    headers["Accept-Language"] = "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5"
    headers["Connection"] = "keep-alive"
    headers["Content-Type"] = "application/json"
    headers["Host"] = "game-api.tl.games"
    # headers["Cache-Control"] = "no-cache"
    # headers["Pragma"] = "no-cache"
    headers["Origin"] = "https://market.tl.games"
    headers["Referer"] = "https://market.tl.games/"
    headers["Sec-Ch-Ua"] = "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
    headers["Sec-Ch-Ua-Mobile"] = "?0"
    headers["Sec-Ch-Ua-Platform"] = "Windows"
    headers["Sec-Fetch-Dest"] = "empty"
    headers["Sec-Fetch-Mode"] = "cors"
    headers["Sec-Fetch-Site"] = "same-site"
    # headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) thunder-lands/0.2.2 Chrome/91.0.4472.164 Electron/13.6.9 Safari/537.36"
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    data = {
        "email": email + '@gmail.com',
        "password": email
    }

    onPrint("Current login data: ", "yellow")
    onPrint("   UserName: " + email, "green")

    time.sleep(1)

    # onPrint("Đang đăng nhập...", "yellow")

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    loginResult = json.loads(respLogin.content)
    headersRes = respLogin.headers

    if (respLogin.status_code == 200):
        # onPrint("   Đăng nhập ngon lành lun!", "green")
        # onPrint(loginResult, "green")
        global accessToken
        accessToken = loginResult['accessToken']
        headers["Authorization"] = accessToken
        # onGetProfile(headersRes['ETag'])
        
    else:
        onPrint("   Login failed!", "red")
        print(loginResult)

def onGetProfile():
    url = "https://game-api.tl.games/auth/profile"
    
    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return result['balances']['crystal']
    else:
        onPrint("   Get profile failed!", "red")
        print(result)

def onGetNft():
    url = "https://game-api.tl.games/game-account/myNft"
    
    respLogin = requests.get(url, headers=headers)
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        return result
    else:
        onPrint("   Get NFT failed!", "red")
        print(result)

def onReturnNftReq():
    url = "https://game-api.tl.games/game-account/return-nft"
    
    data = {
        "items": [
            {
                "itemNftAddress": "0x4fFc239A66Ab22fabC57AC4eED91f39245aCDa8F",
                "itemTokenId": 161
            }
        ],
        "wallet": "0xe10befbad5ff9ce4f7659df6e1c957a475195e84"
    }

    print(data)
    try:
        respLogin = requests.post(url, headers=headers, data=json.dumps(data))
        result = json.loads(respLogin.content)

        if (respLogin.status_code == 200):
            print(result)
            return
        else:
            onPrint("   Return NFT failed!", "red")
            print(result)
    except Exception as e:
        onPrint(e, 'red')
        onReturnNftReq()

def onReturnNft():
    clickBtn(images['sword'], 60)
    clickBtn(images['confirm'], 60)
    time.sleep(10)

def onExchangeTNDR(balance, countWallet):
    url = "https://game-api.tl.games/game-account/TNDR-exchange"

    time.sleep(1)
    # randomWallet = randint(1, 21)
    # randomWallet = randint(0, 6)
    # global resultWithdraw
    # resultWithdraw[str(randomWallet)] = resultWithdraw[str(randomWallet)] + 1

    data = {
        "walletAddress": wallets[countWallet],
        "crystalAmount": balance,
        "token": (solveCaptcha())['code']
    }

    print(data)

    respLogin = requests.post(url, headers=headers, data=json.dumps(data))
    result = json.loads(respLogin.content)

    if (respLogin.status_code == 200):
        if (not result['status']):
            onPrint("   Withdraw fail!", "red")
            print(result)
            return {'status': False, 'error': 0}
            # loading(3600)
            # onExchangeTNDR(balance)
        # if (result['error_key'] != None and result['error_key'] == 'TNDR_EXCHANGE_WITHOUT_NFT_ERROR'):
        #     onPrint("   Withdraw fail!", "red")
        #     return {'status': False, 'error': 'again'}

        onPrint("   Withdraw success!", "green")
        print(result)
        return {'status': True, 'error': 100}
        # print(json.dumps(resultWithdraw, indent=4, sort_keys=False))
    else:
        onPrint("   Withdraw fail!!", "red")
        print(result)

def solveCaptcha():
    api_key = os.getenv('APIKEY_2CAPTCHA', '9d38018037c3173eb09205630a36aa8e')

    solver = TwoCaptcha(api_key)
    
    try:
        result = solver.recaptcha(
            sitekey='6LdR_hIjAAAAABd5KRyNqE-uK9qX_UIi7i5_lFWu',
            url='https://market.tl.games/')
        return result

    except Exception as e:
        onPrint(e, 'red')

currentNumber = 0

def main():
        global images
        images = load_images()
        shuffle(wallets)
        begin = int(open('lastWithdraw.txt', 'r').read())
        global currentNumber
    # try:
        countWallet = 0
        for number in emailObjectNumber:
            if int(number) >= begin:
                isDepositItem = False
                email = emailObjectNumber[number]
                onLogin(email)
                balance = onGetProfile()
                onPrint(balance, 'green')

                if (balance >= 30000):
                    currentNFT = len(onGetNft()['myNft'])
                    onPrint("NFT: " + str(currentNFT), 'yellow')
                    if (currentNFT < 1):
                        isDepositItem = True
                        onPrint(" Loginng by bot...", 'yellow')
                        onLoginByBot(email + '@gmail.com', email)
                        onPutNft()

                    pyautogui.press('f5')

                    time.sleep(3)
                    while(True):
                        if (len(onGetNft()['myNft']) > 0):
                            pyautogui.press('f5')
                            time.sleep(1)
                            break
                        time.sleep(3)
                    
                    # while (True):
                    #     if (pyautogui.locateOnScreen(images['light-exchange']) is not None):
                    #         break
                    #     pyautogui.press('f5')
                    #     time.sleep(10)
                    #     print(1)

                    # print('light-done')

                    # #Hand#######################################################
                        
                    # # while (not checkIsButtonExist(images['light-exchange'])):
                    # #     pyautogui.press('f5')
                    # #     time.sleep(60)
                    
                    # while(True):
                    #     if pyautogui.locateOnScreen(images['sword']) is not None:
                    #         break
                    #     pyautogui.press('f5')
                    #     time.sleep(10)
                    #####################################################

                    onPrint(" Try to withdraw...", 'yellow')
                    while(True):
                        exchangeResponse = onExchangeTNDR(balance, countWallet)
                        # if (exchangeResponse['error'] == 'quit'):
                        #     return
                        if (exchangeResponse['error'] == 0):
                            time.sleep(60)
                            # time.sleep(3)
                            # while(True):
                            #     if (len(onGetNft()['myNft']) > 0):
                            #         break
                        # time.sleep(3)
                        if (exchangeResponse['error'] == 100):
                            break
                    
                    if isDepositItem:
                        while(True):
                            print("return item")
                            onReturnNftReq()
                            pyautogui.press("F5")
                            time.sleep(10)
                            if (checkIsButtonExist(images['dark-exchange'], 0.99) and len(onGetNft()['myNft']) == 0):
                                break
                        
                    onLogout()
                    if (len(onGetNft()['myNft']) > 0):
                        onReturnNftReq()
                    
                    countWallet = countWallet + 1
                    if (countWallet == len(wallets)):
                        countWallet = 0
                        shuffle(wallets)
                
            if int(number) > 1000:
                return
            currentNumber = number
            f = open('lastWithdraw.txt', 'w')
            f.write(str(number))
            f.close()
            
#################################################################################

            # global totalDone
            # listRandom = list(range(0, 5000))
            # random.shuffle(listRandom)
            # for number in listRandom:
            #     email = emailObjectNumber[str(number)]
            #     onLogin(email  + '@gmail.com')
            #     balance = onGetProfile()
            #     onPrint(balance, 'green')
            #     if (balance >= 30000):
            #         onExchangeTNDR(balance)
            #         loading(randint(3, 7))
            #         totalDone = totalDone + 1
            #         onPrint(totalDone, 'green')
        
    # except Exception as e:
    #     onPrint(e, 'red')
    #     begin = int(open('lastWithdraw.txt', 'r').read())
    #     f = open('lastWithdraw.txt', 'w')
    #     f.write(str(currentNumber))
    #     f.close()
    #     main()

main()