import pyautogui
import time

targetSec = 0

pyautogui.moveTo(500, 500)

while True:
# for _ in range(10**9):
    nowTime = time.localtime()
    nowSec = nowTime[5]

    # print(nowSec)

    if nowSec == targetSec:
        pyautogui.click()
        break

