"""
第四章
4-2 LED切換開關
按一下開;按一下關
實驗程式2:用pass達成按一下開;按一下關

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
    #如果開關被按下
    if sw.value() == 0 :
        #取開關狀態反值
        toggle = not toggle
        #設定LED狀態
        led.value(toggle)
        #若開關仍被按著
        while sw.value() == 0:
            pass

    