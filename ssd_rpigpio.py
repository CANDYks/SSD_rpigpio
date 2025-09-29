import RPi.GPIO as GPIO
import time


# 使用 BCM 腳位編號
GPIO.setmode(GPIO.BCM)

# 七段顯示器的段位對應 GPIO 腳位
segments = {
    'a': 17,
    'b': 18,
    'c': 27,
    'd': 22,
    'e': 23,
    'f': 24,
    'g': 25
}

# 設定 GPIO 為輸出
for pin in segments.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# 數字對應 (共陰極 CC )
digits = {
    0: ['a','b','c','d','e','f'],
    1: ['b', 'c'],
    2: ['a', 'b', 'g', 'e', 'd'],
    3: ['a', 'b', 'g', 'c', 'd'],
    4: ['f', 'g', 'b', 'c'],
    5: ['a', 'f', 'g', 'c', 'd'],
    6: ['a', 'f', 'g', 'c', 'd', 'e'],
    7: ['a', 'b', 'c'],
    8: ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
    9: ['a', 'b', 'c', 'd', 'f', 'g']
}

def display_number(num):
    # 先清空
    for pin in segments.values():
        GPIO.output(pin, GPIO.LOW)
    
    # 點亮需要的段
    for seg in digits[num]:
        GPIO.output(segments[seg], GPIO.HIGH)

try:
    while True:
        for num in range(0, 10):
            display_number(num)
            time.sleep(1)  # 每個數字停 1 秒
except KeyboardInterrupt:
    GPIO.cleanup()