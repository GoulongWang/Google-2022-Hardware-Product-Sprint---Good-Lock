# Google 2022 Hardware Product Sprint - Good Lock
Good Lock will prevent bad guys from breaking into your home and alert the house owner by LINE Notify. If you are the house owner, the door will open automatically by facial recognition. Making it easier for you to enter the house and can safely protect your house. 

## Overview
Using Raspberry Pi 3 Model B+ to develop our hardware product **Good Lock**. If there is a person in front of your door, the motion sensor will be triggered and the camera will start face recognition. If you are the house owner, the door will be unlocked automatically. If you are a stranger and try to damage the door, the MPU6050(IMU) will detect the acceleration of the door, and the alarm will start ringing. **Good lock** will send the stranger's photo to the house owner by email and LINE Notify.

Team members：   
Guolong Wang : 相機人臉辨識、System Integration  
Ricky Chen : 陀螺儀計算開門角度&加速規撞擊偵測 + LED蜂鳴器  
Ashley Yang : 內部機構安排、外殼設計、建模&渲染、實體模型製作  
Ting-Chun Hsu : Motion Sensor  
[Kuei-Tien Lee](https://github.com/afien) : 電磁門鎖控制、元件建模、影片Demo  

HPS Mentor：Jing Wu - Google Pixel Hardware Engineer  
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190966280-c3d9bf4c-1b04-4b62-a56e-49d7f3804ff5.jpg" height="400px"/>
<img src="https://user-images.githubusercontent.com/23274642/190966288-ddf9be61-b556-48ce-b14c-b09856aafec3.jpg" height="400px"/>
</p>

### Demo Video
[Presentation Slide](https://docs.google.com/presentation/d/1iHkLe-sbFPiJUKBg0GQMCyVSQ-Jupq_D/edit?usp=sharing&ouid=108033204784682562613&rtpof=true&sd=true)
<p align="center"><a href="http://www.youtube.com/watch?feature=player_embedded&v=OPbGaqSZQcI
" target="_blank"><img src="http://img.youtube.com/vi/OPbGaqSZQcI/0.jpg" 
alt="HPS Team 2 Demo" width="600" border="10" /></a></p>

### Flowchart
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190955863-1d860781-fa05-4067-9a16-f912b6f29c40.png" width="600px"/>
</p> 

### Block Diagram
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190956091-d07f23f1-456c-4dbd-be1b-438be1380572.png" width="600px">
</p>

## Getting Started
### Hardware Requirements
- Raspberry Pi 3 Model B+ 
- Raspberry Pi Camera
- Raspberry Pi Motion Sensor
- MPU6050 Accelerometer and Gyroscope Sensor
- DC 12V Solenoid Door Lock
- 5V Relay
- 12V Power Supply
- Buzzer
- Red LED
- Breadboard
- Wires

### Software Requirements
- Install OpenCV
- Install face_recognition and imutils
### Clone the repository
```
git clone https://github.com/GoulongWang/Google-2022-Hardware-Product-Sprint---Good-Lock.git
```
### Train Your face 
1. Open the file `headshots.py` and change the variable `name` to your name.
2. Run `headshots.py` and take at least 50 photos of yourself.
3. Run `train_faces.py` to start training

### Email and LINE Notify Setting
1. In the file `Email.py`, change `GMAIL_USERNAME` to your email and `GMAIL_PASSWORD` to your [App passwords](https://support.google.com/accounts/answer/185833?hl=en).
2. In the file `functionLib.py`, find the function `lineNotify()` and then replace `token` string to your [LINE Notify token](https://notify-bot.line.me/en/). If the stranger tries to damage the door, you will receive the stranger's photo by LINE Notify.
3. In the file `functionLib.py`, find the function `sentEmail()` and then replace the `sendTo` email with your email. If a stranger walks to the door, you will receive a notice in this email.

### Run Good Lock on Raspberry Pi
```
python3 hps.py
```
