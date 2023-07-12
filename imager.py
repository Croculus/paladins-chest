import os
from ahk import AHK, ActionChain
from PIL import ImageGrab

def main():
    print('Running imager')
    ac = ActionChain()
    ahk = AHK()

    deals = [(183, 579, 534, 643), (540, 579, 887, 643), (893, 579, 1239, 643)]
    win = ahk.win_get(title= 'Paladins (64-bit' )
    if win == None:
        try:
            os.startfile(r''.format(os.getenv('GAME_FILE')))
            win = ahk.win_wait(title = 'Paladins (64-bit', timeout=40)
            win.activate()
            print('window found')
            ac.sleep(40)
            ac.click(700,840)
            ac.sleep(0.5)
            ac.click(122, 443)
            ac.sleep(0.5)
            ac.click(781, 76)
            ac.perform()
            for i in range(len(deals)):
                ss_img = ImageGrab.grab(deals[i])
                ss_img.save("image\deal{}.jpg".format(i+1))
            win.close()
            

            
        except TimeoutError:
            print('Paladins was not found!')
    else: 
        win.activate()
        print('window found')
        ac.click(700,840)
        ac.sleep(0.5)
        ac.click(122, 443)
        ac.sleep(3)
        ac.click(781, 76)
        ac.perform()
        for i in range(len(deals)):
            ss_img = ImageGrab.grab(deals[i])
            ss_img.save("image\deal{}.jpg".format(i+1))
    



