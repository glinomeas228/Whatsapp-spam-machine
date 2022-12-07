import pyautogui, time
pyautogui.hotkey('win','1')
time.sleep(3)
pyautogui.moveTo(x=373, y=79)
pyautogui.click()
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')
time.sleep(7)
pyautogui.moveTo(x=254, y=611)
pyautogui.click()
time.sleep(3)
for loh in range(1000):
         pyautogui.hotkey('ctrl','v')
         pyautogui.press('enter')