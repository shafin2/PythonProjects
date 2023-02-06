import pyautogui
import time


pyautogui.press("win")
time.sleep(1)
pyautogui.write("chrome")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("facebook")
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)
while(True):
    time.sleep(2)
    pyautogui.scroll(-500)