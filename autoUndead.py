43
import cv2
from os import listdir
from random import random, uniform, randint
import numpy as np
import mss
import pyautogui
import time
import yaml
from pyclick import HumanClicker
import pygetwindow

# Load config file.
stream = open("./config.yaml", 'r')
c = yaml.safe_load(stream)
ct = c['threshold']
ch = c['home']
pause = c['time_intervals']['interval_between_moviments']
pyautogui.PAUSE = pause
hc = HumanClicker()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.007

def addRandomness(n, randomn_factor_size=None):
    """Returns n with randomness
    Parameters:
        n (int): A decimal integer
        randomn_factor_size (int): The maximum value+- of randomness that will be
            added to n

    Returns:
        int: n with randomness
    """

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
    hc.move((addRandomness(x, 10), addRandomness(y, 10)), uniform(0.3, 0.5))

def remove_suffix(input_string, suffix):
    """Returns the input_string without the suffix"""

    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

def load_images(dir_path='./targets'):
    """ Programatically loads all images of dir_path as a key:value where the
        key is the file name without the .png suffix

    Returns:
        dict: dictionary containing the loaded images as key:value pairs.
    """

    file_names = listdir(dir_path)
    targets = {}
    for file in file_names:
        path = 'targets/' + file
        targets[remove_suffix(file, '.png')] = cv2.imread(path)

    return targets

def show(rectangles, img = None):
    """ Show an popup with rectangles showing the rectangles[(x, y, w, h),...]
        over img or a printSreen if no img provided. Useful for debugging"""

    if img is None:
        with mss.mss() as sct:
            monitor = sct.monitors[0]
            img = np.array(sct.grab(monitor))

    for (x, y, w, h) in rectangles:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255,255,255,255), 2)

    # cv2.rectangle(img, (result[0], result[1]), (result[0] + result[2], result[1] + result[3]), (255,50,255), 2)
    cv2.imshow('img',img)
    cv2.waitKey(0)


def clickBtn(img, timeout=3, threshold = ct['default']):
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
        moveToWithRandomness(pos_click_x, pos_click_y, 1)
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
        global images
        images = load_images()
        windows = []

        win = [w for w in pygetwindow.getWindowsWithTitle('Command Prompt')]

        for w in win:
            windows.append({
                "window": w,
            })

        i = 0

        j = i + 999999
        
        time.sleep(1)

        for last in windows:
            # isClicked = clickBtn(images['target'], 0)

            last["window"].activate()
            isClicked = True
            time.sleep(1)
            if isClicked:
                pyautogui.press("c")
                pyautogui.press("d")
                pyautogui.press("space")
                pyautogui.press("c")
                pyautogui.press(":")
                pyautogui.press("\\")

                pyautogui.press("u")
                pyautogui.press("s")
                pyautogui.press("e")
                pyautogui.press("r")
                pyautogui.press("s")

                pyautogui.press("\\")

                pyautogui.press("t")
                pyautogui.press("u")
                pyautogui.press("a")
                pyautogui.press("n")
                pyautogui.press("n")

                pyautogui.press("\\")

                pyautogui.press("d")
                pyautogui.press("o")
                pyautogui.press("c")
                pyautogui.press("u")
                pyautogui.press("m")
                pyautogui.press("e")
                pyautogui.press("n")
                pyautogui.press("t")
                pyautogui.press("s")

                # pyautogui.hotkey('ctrl', 'v')

                pyautogui.press("enter")

                pyautogui.press("p")
                pyautogui.press("y")
                pyautogui.press("t")
                pyautogui.press("h")
                pyautogui.press("o")
                pyautogui.press("n")

                pyautogui.press("space")

                pyautogui.press("u")
                pyautogui.press("n")
                pyautogui.press("d")
                pyautogui.press("e")
                pyautogui.press("a")
                pyautogui.press("d")
                pyautogui.press(".")
                pyautogui.press("p")
                pyautogui.press("y")

                pyautogui.press("enter")
                
                if i == j:
                    break

                i = i + 1
                time.sleep(1)

    except Exception as e:
        print(e)
        main()

main()

