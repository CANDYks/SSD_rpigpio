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

# LED 腳位
LED_PIN = 4
LED2_PIN = 20

#buzzer
buzzer_PIN = 21


# 設定 GPIO 為輸出
for pin in segments.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# 設定 LED 腳位為輸出
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.output(LED2_PIN, GPIO.LOW)

# 設定 buzzer 腳位為輸出
GPIO.setup(buzzer_PIN, GPIO.OUT)
GPIO.output(buzzer_PIN, GPIO.LOW)
# 數字對應 (共陰極 CC → HIGH=亮；若是共陽極 CA 請把 1/0 顛倒)
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
    # 先清空七段顯示器
    for pin in segments.values():
        GPIO.output(pin, GPIO.LOW)
    
    # 點亮需要的段
    for seg in digits[num]:
        GPIO.output(segments[seg], GPIO.HIGH)
    
    # 點亮 LED
    GPIO.output(LED_PIN, GPIO.HIGH)
def display_buzzer():
    GPIO.output(buzzer_PIN, GPIO.HIGH)
    GPIO.output(LED2_PIN, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(buzzer_PIN, GPIO.LOW)
    GPIO.output(LED2_PIN, GPIO.LOW)
try:
    while True:
        # 取得使用者輸入
        user_input = input("請輸入 0-9 的數字 (輸入 q 退出): ")
        
        if user_input.lower() == 'q':
            break
            
        # 檢查輸入是否為有效數字
        try:
            num = int(user_input)
            if num in range(0, 10):
                display_number(num)
                time.sleep(1)  # 顯示 1 秒
                # 關閉 LED 和七段顯示器
                GPIO.output(LED_PIN, GPIO.LOW)
                for pin in segments.values():
                    GPIO.output(pin, GPIO.LOW)
            else:
                print("請輸入 0-9 的數字！")
        except ValueError:
            print("無效輸入，請輸入 0-9 的數字！")
            display_buzzer()
except KeyboardInterrupt:
    print("\n程式終止")
finally:
    GPIO.cleanup()