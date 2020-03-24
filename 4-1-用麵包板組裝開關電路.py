"""
第四章
4-1 用麵包板組裝開關電路
"""

#從"machine"匯入"Pin"類別的方式
from machine import Pin

#LED接腳(輸出)
led = Pin(2, Pin.OUT)

#開關接腳(輸入)
sw = Pin(0, Pin.IN)

#反覆讀取開關狀態並設定燈光
while True:
    #讀取開關值
    val = sw.value()
    #設定燈光
    led.value(val)
    