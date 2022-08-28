#! /usr/bin/python

from gpiozero import MotionSensor
from imutils.video import VideoStream
import RPi.GPIO as GPIO
import face_recognition
import imutils
import pickle
import time
import cv2
from functionLib import *

# 紅外線感測腳位
pir = MotionSensor(4)

# 繼電器腳位
relay = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

# Buzzer 設定
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)

encodingsP = "encodings.pickle"
data = pickle.loads(open(encodingsP, "rb").read())
vs = VideoStream(src=0, framerate=10).start()
#vs = VideoStream(usePiCamera=True).start()
print("[INFO] 專業顧門口啟動中")

while True:
    time.sleep(1)
    if pir.motion_detected:
        print("[INFO] Good Looking Person Detected")
        currentname = "unknown"
        lock = False
        Stranger = False

        while True:
            frame = vs.read()
            frame = imutils.resize(frame, width=500)
            boxes = face_recognition.face_locations(frame)
            encodings = face_recognition.face_encodings(frame, boxes)
            names = []

            for encoding in encodings:
                matches = face_recognition.compare_faces(
                    data["encodings"], encoding)
                name = "陌生人"

                if True in matches:
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}

                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1

                    name = max(counts, key=counts.get)

                    if currentname != name:
                        currentname = name
                        print("[INFO] " + currentname + " 回家了")
                        doorOpen_Close(relay)
                        lock = True
                        break
                else:
                    # 是陌生人就開啟加速
                    '''
                    if 門被打開:
                        # 蜂鳴器呼叫
                        while True:
                            GPIO.output(buzzer, GPIO.HIGH)
                            print ("[ALERT] 陌生人入侵家中 ! ")
                            time.sleep(0.5) 
                            GPIO.output(buzzer, GPIO.LOW)
                            time.sleep(0.5)

                        # LED 閃爍

                        # 拍一張照片
                        # 錄影 (還沒寫)
                        # 用 Line 通知家人
                        # 寄信通知家人
                    '''
                    Stranger = True
                    image = vs.read()
                    takePhoto(image)
                    lineNotify()
                    sentEmail()
                    break

                names.append(name)

            # 框臉
            for ((top, right, bottom, left), name) in zip(boxes, names):
                cv2.rectangle(frame, (left, top), (right, bottom),
                              (0, 255, 225), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                            .8, (0, 255, 255), 2)

            cv2.imshow("人臉辨識啟動", frame)
            key = cv2.waitKey(1) & 0xFF  # cant delete

            if lock or Stranger:
                break

        cv2.destroyAllWindows()
        # vs.stop()
    else:
        print('[INFO] Nobody')
