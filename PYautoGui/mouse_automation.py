import pyautogui

# PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui.FailSafeException exception.
pyautogui.FAILSAFE=False

# To show screen size
print(pyautogui.size())

# To show mouse position
# pyautogui.displayMousePosition()

# to move cursor (x,y,duration=sec)
# pyautogui.moveTo(0,768,duration=5)

# To automatic click
# parameters are (x,y,button,clicks,duration)
# pyautogui.click(x=1368,y=2,button='left',clicks=1,duration=3)

# To drag/select
# parameters(x,y,time)
# pyautogui.dragTo(100,100,duration=5)

# For scrolling
# parameters for (-value) it scrolls down and vice versa
# (-500) mean scroll down ten click
pyautogui.scroll(-500)




# pyautgui.size()
# pyautogui.position()
#  pyautiogui.displayMousePosition()
#  pyautogui.moveTo()
# pyautogui.click(), doubleclick() , tripleclick()
#  pyautogui.dragTo()
# pyautogui.dragRel()
# pyautogui.FAILSAFE
# pyautogui.Scroll()