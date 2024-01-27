import pyautogui
pyautogui.size() # returns the size of the screen we are working on
width, height = pyautogui.size()

pyautogui.position() # returns current mouse location
pyautogui.moveTo(10,10, duration=5) # moves mouse to coordinates in specified time frame

pyautogui.moveRel(25,25, duration=2.5) #moves mouse relative to current postion
pyautogui.moveRel(0, -100, duration=1) #moves mouse UP 100 pixels

pyautogui.click(1316,489) # click specified coordinates
pyautogui.doubleClick() #double clicks in position
pyautogui.rightClick() # right clicks in position

pyautogui.dragRel(distanceX, distanceY, duration=3) # drags specified distances