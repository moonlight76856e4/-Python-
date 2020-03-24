"""
第四章
4-2 LED切換開關
"""

#從"machine"匯入"Pin"類別的方式
from machine import Pin

#開關狀態預設高電位
toggle = 1

#LED接腳(輸出)
led = Pin(2, Pin.OUT)

#開關接腳(輸入)
sw = Pin(0, Pin.IN)

#反覆讀取開關狀態並設定燈光
while True:
    if sw.value() == 0 :
        toggle = not toggle
        led.value(toggle)

    