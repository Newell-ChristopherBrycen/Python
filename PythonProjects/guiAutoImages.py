import pyautogui

pyautogui.screenshot('c:\\users\\bryne\\downloads\\screenshot_example.png')
pyautogui.locateOnScreen('c:\\users\\bryne\\downloads\\calc7key.png') #references mentioned image and then identifies the coordinates of that image on the current screenshot
pyautogui.locateCenterOnScreen('c:\\users\\bryne\\downloads\\calc7key.png') # same as above but with center of object coordinates

#you can use this in coordination with the 'moveTo' and 'click' functions to select items found that match the prepared image


