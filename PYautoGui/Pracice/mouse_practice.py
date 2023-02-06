import pyautogui

def show_desktop(screen_width,screen_hieght):
    pyautogui.click(x=screen_width, y=screen_hieght, button='left', clicks=1, duration=2)

if __name__ == '__main__':
    pyautogui.FAILSAFE = False
    a = pyautogui.size()
    screen_width = a[0]
    screen_hieght = a[1]
    show_desktop(screen_width,screen_hieght)
    pyautogui.click(x=512, y=745, button='left', clicks=2, duration=5)
    pyautogui.moveTo(255, 216, duration=2)
    pyautogui.dragTo(455, 216, duration=2)
    pyautogui.dragTo(455, 416, duration=2)
    pyautogui.dragTo(255, 416, duration=2)
    pyautogui.dragTo(255, 216, duration=2)

