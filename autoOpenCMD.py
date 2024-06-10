# -*- coding: utf-8 -*-    
# from src.logger import logger, loggerMapClicked
import cv2
from os import listdir
from random import random, uniform, randint
import numpy as np
import mss
import pyautogui
import time
import yaml

# Load config file.
stream = open("./config.yaml", 'r')
c = yaml.safe_load(stream)
ct = c['threshold']
ch = c['home']
pause = c['time_intervals']['interval_between_moviments']
pyautogui.PAUSE = pause
# hc = HumanClicker()
pyautogui.FAILSAFE = False


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


def addRandomness(n, randomn_factor_size=None):
    if randomn_factor_size is None:
        randomness_percentage = 0.1
        randomn_factor_size = randomness_percentage * n

    random_factor = 2 * random() * randomn_factor_size
    if random_factor > 5:
        random_factor = 5
    without_average_random_factor = n - randomn_factor_size
    randomized_n = int(without_average_random_factor + random_factor)
    # logger('{} with randomness -> {}'.format(int(n), randomized_n))
    return int(randomized_n)

def moveToWithRandomness(x,y,t):
    a = 1
    # hc.move((addRandomness(x, 10), addRandomness(y, 10)), uniform(0.01, 0.05))
    pyautogui.moveTo(addRandomness(x, 10), addRandomness(y, 10), uniform(0.001, 0.003))


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
        pos_click_x = x+w/uniform(1, 3)
        pos_click_y = y+h/uniform(1, 3)
        moveToWithRandomness(pos_click_x,pos_click_y,1)
        pyautogui.click()
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

def main():
    try:
        images = load_images()
        for i in range(0, 30):
            while(True):
                if (checkIsButtonExist(images['search'])):
                    break
            clickBtn(images['search'], 15)
            pyautogui.press('c')
            pyautogui.press('m')
            pyautogui.press('d')
            pyautogui.press('enter')
    except Exception as e:
        print(e)

main()
#cv2.imshow('img',sct_img)
#cv2.waitKey()

# colocar o botao em pt
# soh resetar posiçoes se n tiver clickado em newmap em x segundo

# if now - last["heroes"] > addRandomness(t['send_heroes_for_work'] * 60) or isStruck['status']:
#                     last["window"].activate()
#                     last["heroes"] = now
#                     refreshHeroes(last['account'])
#                     last["refresh_heroes"] = now


