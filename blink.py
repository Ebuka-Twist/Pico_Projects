import machine
import utime
LED = machine.Pin(25,machine.Pin.OUT)
for i in range(20):
    LED.value(1)
    utime.sleep(1)
    print(LED.value())
    LED.value(0)
    utime.sleep(1)
    print(LED.value())