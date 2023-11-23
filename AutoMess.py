import pyautogui 
import time
time.sleep(5)
pyautogui.typewrite('www.facebook.com/messages/t/100029088600729')
time.sleep(1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.leftClick(263, 447, 1, 1)
time.sleep(1)
for i in range(1):
    pyautogui.typewrite("*")
    pyautogui.press('enter')
print('Success!')