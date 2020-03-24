"""
第三章
3-2 自行連接LED

從"machine"匯入"Pin"類別的方式

在第16腳接LED

"""

#從"machine"匯入"Pin"類別
from machine import Pin

#匯入"time"模組才能執行sleep()
import time

#在16腳輸出高電位
led = Pin(16, Pin.OUT)

#腳16輸出高電位(亮燈)
led.value(1)

#腳16輸出低電位(不亮燈)
led.value(0)

for i in range(3):
    led.value(0)
    time.sleep(0.5)
    led.value(1)
    time.sleep(0.5)