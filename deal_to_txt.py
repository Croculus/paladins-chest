import os
from ahk import AHK, ActionChain


ac = ActionChain()
ahk = AHK()

win = ahk.active_window           

run= os.startfile(r'com.epicgames.launcher://apps/badb0ee71b474ed591ec43212547cfc8%3A85a98d012e1245c8a6572f03fcf920b6%3AAntbird?action=launch&silent=true')

try: 
    win = ahk.win_wait(title = 'Paladins (64-bit, DX11)', timeout=40)#doesn't work idk why
    win.activate()#doesn't work idk why
    ac.sleep(15)
    ac.click(122, 443)
    ac.sleep(3)
    ac.click(781, 76)
    print('yes')
    
except TimeoutError:
    print("No Paladins")

