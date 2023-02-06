import pyautogui
import time


# pyautogui.FAILSAFE = False
# a = pyautogui.size()
# screen_width = a[0]
# screen_hieght = a[1]
# pyautogui.click(x=screen_width, y=screen_hieght, button='left', clicks=1, duration=2)
# time.sleep(1)
pyautogui.press("win")
time.sleep(1)
pyautogui.write("calculator")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.click(pyautogui.locateOnScreen("C:\\Users\\HUZAIFA CCTV CAMERA\\Desktop\\5.png",confidence=.9))
pyautogui.click(pyautogui.locateOnScreen("C:\\Users\\HUZAIFA CCTV CAMERA\\Desktop\\o.png",confidence=.9))

