# Google 2022 Hardware Product Sprint - Good Lock
Good Lock will prevent bad guys break into your home and alert the house owner by LINE Notify. If you are the house owner, the door will open automatically by facial recognition. Make it easier for you to enter the house and protect your house safely. 

## Overview
We used Raspberry Pi 3 Model B+ to develop our product **Good Lock**. If there is a person in front of your house, the motion sensor will be triggered. At the same time, the camera will start face recognition. If you are the house owner, the door will be unlock automatically. If you are a stranger and try to enter the house, the MPU6050 accelerometer and gyroscope sensor will detect the changes of the door, and the alarm will start ringing and notify the house owner. The system will take a photo of the stranger and sent the photo to the house owner by email and Line Notify.

Team members：Guolong Wang, Ashley Yang, Ting-Chun Hsu, Ricky Chen, Kuei-Tien Lee  
HPS Mentor：Jing Wu - Google Pixel Hardware Engineer  
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190966280-c3d9bf4c-1b04-4b62-a56e-49d7f3804ff5.jpg" height="400px"/>
<img src="https://user-images.githubusercontent.com/23274642/190966288-ddf9be61-b556-48ce-b14c-b09856aafec3.jpg" height="400px"/>
</p>

### Demo Video
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
```
### Train Your face 
1. Open the file `headshots.py` and change the variable `name` to your name.
2. Run `headshots.py` and take at least 50 photos of yourself.
3. Run `train_faces.py` to start training
### Run Good Lock on Raspberry Pi
```
python3 hps.py
```

### HPS Certification
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/191014841-05cee3a9-ddd3-4e8a-b6a0-314cb4eeb1ae.jpg" width="600px">
</p>
