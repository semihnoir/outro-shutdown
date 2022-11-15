import os
import time as tm
from pygame import mixer
mixer.init()
mixer.music.load('kaynaklar/outromeme.mp3')
mixer.music.play()
j = 14

for sayac in range(14):
    
    print(f"Bilgisayarınız {j} saniye içinde kapatılacak.")
    j-=1
    tm.sleep(1)

if j == 0:
    print("Bilgisayar kapatılıyor.")
    tm.sleep(1.5)
    os.system("shutdown /s /t 1")
    
# Art by Semih Noir
    


