"""
第三章
3-21 Singnal類別設定正反像輸出值

從"machine"匯入"Pin"類別的方式

使用Singal將自動反轉輸出狀態

"""

#從"machine"匯入"Pin"類別及"Signal"類別
from machine import Pin, Signal

#把第2腳(D4)設為輸出預設成高電位(不亮燈)
ledPin = Pin(2, Pin.OUT, value=1)

#Singal(Pin物件,invert=是否相反)
led = Signal(ledPin, invert=True)

#腳2輸出低電位(不亮燈)
led.value(0)

#腳2輸出高電位(亮燈)
led.value(1)

#亮燈
led.on()

#不亮燈
led.off()
