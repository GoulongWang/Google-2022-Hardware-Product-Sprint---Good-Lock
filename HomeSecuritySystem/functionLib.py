from Email import Emailer
import RPi.GPIO as GPIO
import cv2
import requests
import smtplib
import time


def doorOpen_Close(relay):
    GPIO.output(relay, 1)
    print("[INFO] 已解鎖家門")
    time.sleep(10)
    print('[INFO] 10 秒後自動上鎖')
    GPIO.output(relay, 0)
    print('[INFO] 已上鎖家門')


def takePhoto(img):
    print('[INFO] 可疑人照片已紀錄')
    cv2.imwrite('/home/guolong/Desktop/Stranger.jpg', img)


def lineNotify():
    url = "https://notify-api.line.me/api/notify"
    token = "nOI8ho96jhuS7OQ5YljoT37ksDFvqA0AMgQ3cRgCumX"
    headers = {"Authorization": "Bearer " + token}
    msg = {"message": "陌生人入侵 !"}
    files = {'imageFile': open('/home/guolong/Desktop/Stranger.jpg', 'rb')}
    req = requests.post(url, headers=headers, data=msg, files=files)


def sentEmail():
    sender = Emailer()
    sendTo = 'guolongwang2022@hps-program.com'
    emailSubject = "[ALERT] A Stranger is breaking into your house."
    emailContent = "There is a stranger in front of your house!"
    sender.sendmail(sendTo, emailSubject, emailContent)
    print('[ALERT] 陌生人入侵 ! ')
