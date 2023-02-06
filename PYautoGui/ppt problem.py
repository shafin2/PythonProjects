import pyautogui
import  time

nmbr_of_slides=int(input("How mant slides do you want ??"))
for i in range(nmbr_of_slides):
    time.sleep(5)
    pyautogui.click(x=1233, y=348, button='left', clicks=1)
    time.sleep(0.5)
    pyautogui.press("delete")
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)
    pyautogui.click(x=437, y=43, button='left', clicks=1)
    time.sleep(0.5)
    pyautogui.click(x=940, y=75, button='left', clicks=1)
    time.sleep(0.5)
    for i in range(12):
        pyautogui.click(x=1311, y=217, button='left', clicks=20)
        time.sleep(0.5)
    time.sleep(0.5)
    pyautogui.click(x=1341, y=179, button='left', clicks=1)
    time.sleep(0.5)
    pyautogui.click(x=84, y=42, button='left', clicks=1)
    pyautogui.click(x=273, y=229, button='left', clicks=1)
    time.sleep(1)
    pyautogui.press("down")


#
# pyautogui.hotkey('ctrl','v')
# with pyautogui.hold('shift'):
#     pyautogui.click(x=355, y=512, button='left', clicks=1)
#     pyautogui.click(x=357, y=355, button='left', clicks=1)
#     pyautogui.click(x=720, y=181, button='left', clicks=1)
#     pyautogui.click(x=887, y=178, button='left', clicks=1)
#     pyautogui.click(x=1217, y=322, button='left', clicks=1)
#     pyautogui.click(x=1224, y=448, button='left', clicks=1)
#     pyautogui.click(x=875, y=616, button='left', clicks=1)
#     pyautogui.click(x=697, y=611, button='left', clicks=1)
#     # pyautogui.moveTo(343,486)
#     # pyautogui.moveTo(345,314)
# #     pyautogui.press(['left', 'left', 'left'])
# # pyautogui.displayMousePosition()
#
# time.sleep(5)
# pyautogui.press("delete")