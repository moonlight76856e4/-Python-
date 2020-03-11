"""
第三章
3-1 Micropython基本操作

從"machine"匯入"Pin"類別的方式

"""
#從"machine"匯入"Pin"類別
from machine import Pin

#匯入"time"模組才能執行sleep()
import time

#把第2腳(D4)設為輸出
p2 = Pin(2, Pin.OUT)

#把第2腳(D4)設為輸出預設成低電位(亮燈)
p2 = Pin(2, Pin.OUT, value=0)

#把第2腳(D4)設為輸出預設成低電位(不亮燈)
p2 = Pin(2, Pin.OUT, value=1)



#腳2輸出低電位(亮燈)
p2.value(0)

#腳2輸出低電位(不亮燈)
p2.value(1)

#腳2輸出低電位(亮燈)
p2.off()

#腳2輸出低電位(不亮燈)
p2.on()

#持續0.5秒
time.sleep(0.5)

#燈光閃滅3次，每次閃滅持續時間0.5秒
for i in range(3):
    p2.value(0)
    time.sleep(0.5)
    p2.value(1)
    time.sleep(0.5)

#使用while讓腳2的LED燈不停閃爍
#True可改成1
while True:
    p2.value(0)
    time.sleep(0.5)
    p2.value(1)
    time.sleep(0.5)





