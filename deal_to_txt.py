import os, time
from ahk.window import Window
from ahk import AHK, ActionChain
from PIL import ImageGrab


ac = ActionChain()
ahk = AHK()

win = ahk.active_window           

#run= os.startfile(r'com.epicgames.launcher://apps/badb0ee71b474ed591ec43212547cfc8%3A85a98d012e1245c8a6572f03fcf920b6%3AAntbird?action=launch&silent=true')

print('y')
ss_region = (172, 185, 1251, 651)
ss_img = ImageGrab.grab(ss_region)
ss_img.save("image\deal.jpg")
'''
try:
    win = ahk.win_wait(title = 'Paladins (64-bit', timeout=40)#doesn't work idk why
    win.activate()#doesn't work idk why
    print('yes')
    ac.sleep(45)
    ac.click(122, 443)
    ac.sleep(3)
    ac.click(781, 76)
    ac.perform()

    
except TimeoutError:
    print('Notepad was not found!')
'''