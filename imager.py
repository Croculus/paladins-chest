import os
from ahk import AHK, ActionChain
from PIL import ImageGrab

def main():
    ac = ActionChain()
    ahk = AHK()

    win = ahk.active_window           
    #run= os.startfile(r'com.epicgames.launcher://apps/badb0ee71b474ed591ec43212547cfc8%3A85a98d012e1245c8a6572f03fcf920b6%3AAntbird?action=launch&silent=true')
    print('y')

    deals = [(183, 579, 534, 643), (540, 579, 887, 643), (893, 579, 1239, 643)]
    for i in range(len(deals)):
            ss_img = ImageGrab.grab(deals[i])
            ss_img.save("image\deal{}.jpg".format(i+1))
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
        print('Paladins was not found!')
    '''



