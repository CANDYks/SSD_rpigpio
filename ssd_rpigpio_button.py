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
    # 清空
    for pin in segments.values():
        GPIO.output(pin, GPIO.LOW)
    # 點亮需要的段
    for seg in digits[num]:
        GPIO.output(segments[seg], GPIO.HIGH)

# ===== 按鈕與蜂鳴器設定 =====
BUTTON_PIN = 5   
BUZZER_PIN = 21   

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.output(BUZZER_PIN, GPIO.LOW)

def beep(duration=0.2):
    """讓蜂鳴器發出嗶聲"""
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

current_num = 0
display_number(current_num)

try:
    press_time = None
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # 按下
            if press_time is None:
                press_time = time.time()  # 記錄開始時間
            time.sleep(0.01)
        else:  # 放開
            if press_time is not None:
                duration = time.time() - press_time
                if duration >= 2:  # 長按歸零
                    current_num = 0
                    beep(0.5)  # 嗶 0.5 秒提示
                else:  # 短按加 1
                    current_num = (current_num + 1) % 10
                display_number(current_num)
                press_time = None
            time.sleep(0.01)
except KeyboardInterrupt:
    GPIO.cleanup()
