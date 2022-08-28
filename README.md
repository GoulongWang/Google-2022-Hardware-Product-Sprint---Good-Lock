# Google 2022 Hardware Product Sprint - Home Security System
Home Security System (專業顧門口) will prevent bad guys break into your home and alert the house owner. If you are the house owner, the door will open automatically by facial recognition. Make it easier for you to enter the house and protect your house safely. 

## Overview
We used Raspberry Pi 3 Model B+ to develop our Home Security System (專業顧門口). If there is a person in front of your house, the motion sensor will be triggered. At the same time, the camera will start face recognition. If you are the house owner, the door will be unlock automatically. If you are a stranger and try to enter the house, the MPU6050 accelerometer and gyroscope sensor will detect the changes of the door, and the alarm will start ringing and notify the house owner. 

Contibuters：Guolong Wang, Ashley Yang, Ting-Chun Hsu, Ricky Chen, Kuei-Tien Lee  
HPS Mentor：Jing Wu - Google Pixel Hardware Engineer  
### Flowchart
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/187068578-d3c81000-d83e-4bd9-97dc-540c8edffdad.png" />
</p>  

### Block Diagram
<p align="center">
<img src="https://user-images.githubusercontent.com/23274642/186562664-f117c5c7-3981-4216-ad2e-177884fa7e14.png">
</p>

## Getting Started
### Hardware Requirements
- Raspberry Pi 3 Model B+ 
- Raspberry Pi Camera
- USB Webcam
- Raspberry Pi Motion Sensor
- MPU6050 Accelerometer and Gyroscope Sensor
- DC 12V Solenoid Door Lock
- 5V Relay
- 12V Power Supply
- Buzzer
- Red LED
- Breadboard
- Wires (male to male, female to female)

### Install Libraries on Raspberry Pi
```
sudo apt install cmake build-essential pkg-config git
```
### Clone the repository
### Run Home Security System on Raspberry Pi
