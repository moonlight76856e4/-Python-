"""
第四章
4-2 LED切換開關
按一下開;按一下關
實驗程式3_1:
不使用toggle變數來記錄開關狀態
但使用讀取LED的狀態再取相反值會出現機械式開關的彈跳現象
造成LED亮的時候不亮；關的時候未關
用程式解決彈跳問題

"""

#匯入時間模組
import time

#從"machine"匯入"Pin"類別的方式
from machine import Pin

#LED接腳(輸出)
led = Pin(2, Pin.OUT)

#開關接腳(輸入)
sw = Pin(0, Pin.IN)

#反覆讀取開關狀態並設定燈光
while True:
    #如果開關被按下
    if sw.value() == 0 :
        #先暫停20毫秒
        time.sleep_ms(20)
        #暫停之後再次確認輸入值
        if sw.value() == 0 :
            #讀取LED的狀態再取相反值
            led.value(not led.value())
            #若開關仍被按著
            while sw.value() == 0:
                pass

    