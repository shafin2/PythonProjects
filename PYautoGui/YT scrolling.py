import pyautogui
import keyboard
while True:
    if keyboard.is_pressed("esc"):
        pyautogui.press("down")
    if keyboard.is_pressed("`"):
        break