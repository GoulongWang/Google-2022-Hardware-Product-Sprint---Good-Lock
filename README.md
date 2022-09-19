# Google 2022 Hardware Product Sprint - Good Lock
Good Lock will prevent bad guys break into your home and alert the house owner by LINE Notify. If you are the house owner, the door will open automatically by facial recognition. Make it easier for you to enter the house and protect your house safely. 

## Overview
We used Raspberry Pi 3 Model B+ to develop our product **Good Lock**. If there is a person in front of your house, the motion sensor will be triggered. At the same time, the camera will start face recognition. If you are the house owner, the door will be unlock automatically. If you are a stranger and try to enter the house, the MPU6050 accelerometer and gyroscope sensor will detect the changes of the door, and the alarm will start ringing and notify the house owner. The system will take a photo of the stranger and sent the photo to the house owner by email and Line Notify.

Contibuters：Guolong Wang, Ashley Yang, Ting-Chun Hsu, Ricky Chen, Kuei-Tien Lee  
HPS Mentor：Jing Wu - Google Pixel Hardware Engineer  
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190966288-ddf9be61-b556-48ce-b14c-b09856aafec3.jpg" />
</p> 

<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190966280-c3d9bf4c-1b04-4b62-a56e-49d7f3804ff5.jpg" />
</p> 

### Flowchart
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190955863-1d860781-fa05-4067-9a16-f912b6f29c40.png" />
</p> 

<img src="https://user-images.githubusercontent.com/23274642/187185451-e2ce89c8-7864-4715-b84f-0ad98e72cbbc.jpg" width="200"/>

<img src="https://user-images.githubusercontent.com/23274642/187209102-835dd727-efce-46fb-9a35-c1a90a4cb3de.jpg" width="200"/>

<img src="https://user-images.githubusercontent.com/23274642/187209190-8bd17112-7a35-4862-8b41-9b30f8556689.jpg" width="200"/>

<img src="https://user-images.githubusercontent.com/23274642/187209250-1efec31c-ed55-46f9-8b45-92c9e58961d8.jpg" width="200"/>

<img src="https://user-images.githubusercontent.com/23274642/187209262-55089710-99f9-42e8-8587-d330e6b59d57.jpg" width="200"/>

<img src="https://user-images.githubusercontent.com/23274642/187209353-9c5a9ac9-18dc-40eb-a4d2-9b4b04946aa5.jpg" width="200"/>

### Block Diagram
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/190956091-d07f23f1-456c-4dbd-be1b-438be1380572.png">
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

### Demo
### Certification
