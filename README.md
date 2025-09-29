# 七段顯示器實驗 (Raspberry Pi)

## 專案說明

本專案使用 **Raspberry Pi** 搭配 **共陰極（CC, Common Cathode）七段顯示器**，實作輸入數字顯示功能。

* 使用者可輸入 0–9 的數字，對應顯示於七段顯示器。
* 若輸入非數字，系統會觸發蜂鳴器與 LED 警示。

---

## 硬體資訊

* **七段顯示器 (Common Cathode, CC)**
* **Raspberry Pi 4 Model B** (或其他支援 GPIO 的樹莓派版本)
* LED × 2
* 蜂鳴器 × 1
* 杜邦線、電阻

---

## 腳位對應 (Pin Mapping)

七段顯示器段位  Raspberry Pi GPIO 腳位 

 a,GPIO 17 
 b,GPIO 18              
 c,GPIO 27              
 d,GPIO 22              
 e,GPIO 23              
 f,GPIO 24              
 g,GPIO 25              

其他元件：

* LED1：GPIO 4
* LED2：GPIO 20
* 蜂鳴器：GPIO 21

---

## 使用方法

1. 確認已安裝 **RPi.GPIO**：

   ```bash
   pip install RPi.GPIO
   ```
2. 將接線完成（見 wiring photo）。
3. 執行程式：

   ```bash
   python3 ssd_rpigpio.py
   ```
4. 依照提示輸入數字：

   * 輸入 `0–9` → 七段顯示器顯示對應數字
   * 輸入非數字 → LED2 與蜂鳴器警示
   * 輸入 `q` → 離開程式

---

## 接線圖／實際接線照片

<table>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/89aedb2e-2dfc-4fd5-9daa-8317de557aa9" alt="441652" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/5a7c5af2-157d-41b6-a693-9952d13bf90c" alt="441651_0" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/3aaa05f6-69de-492d-917b-e15a9c5702b1" alt="441650_0" width="300"></td>
    <td><img src="https://github.com/user-attachments/assets/257d7b4d-c11a-4398-bacc-530d3f7b078f" alt="441649_0" width="300"></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/33973d2c-ed14-4f64-aaf4-33f99431e73b" alt="441648_0" width="300"></td>
    <td></td>
  </tr>
</table>

## 注意事項

* 本程式碼依照 **共陰極（CC）邏輯設計**：輸出 HIGH 時對應段位亮起。
* 若使用 **共陽極（CA）** 七段顯示器，需將輸出反相（HIGH ↔ LOW）。
* 程式中使用 `GPIO.cleanup()`，確保結束時釋放 GPIO。
