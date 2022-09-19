from Email import Emailer
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import cv2
import requests
import smtplib
import time
import smbus
from MPU6050 import *


def takePhoto(img):
    print('[INFO] 可疑人照片已紀錄')
    cv2.imwrite('/home/rick860917/Desktop/Stranger.jpg', img)


def lineNotify():
    url = "https://notify-api.line.me/api/notify"
    token = ""  # Replace your line Notify token
    headers = {"Authorization": "Bearer " + token}
    msg = {"message": "陌生人入侵 !"}
    files = {'imageFile': open('/home/rick860917/Desktop/Stranger.jpg', 'rb')}
    req = requests.post(url, headers=headers, data=msg, files=files)


def sentEmail():
    sender = Emailer()
    sendTo = 'guolongwang2022@hps-program.com'  # You can replace this email.
    emailSubject = "[ALERT] A Stranger is breaking into your house."
    emailContent = "There is a stranger in front of your house!"
    sender.sendmail(sendTo, emailSubject, emailContent)
    print('[ALERT] 陌生人入侵 ! ')


def led_buzzer(buzzer, R, G, B):
    try:
        t = 0.1
        cnt = 0
        pwmR = GPIO.PWM(R, 70)
        pwmG = GPIO.PWM(G, 70)
        pwmB = GPIO.PWM(B, 70)

        pwmR.start(0)
        pwmG.start(0)
        pwmB.start(0)

        while True:
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(buzzer, GPIO.OUT)
            GPIO.output(buzzer, True)
            time.sleep(t)
            GPIO.output(buzzer, False)
            GPIO.cleanup(buzzer)

            GPIO.setup(R, GPIO.OUT)
            GPIO.setup(G, GPIO.OUT)
            GPIO.setup(B, GPIO.OUT)

            pwmR.ChangeDutyCycle(0)
            pwmG.ChangeDutyCycle(100)
            pwmB.ChangeDutyCycle(100)
            time.sleep(t)
            cnt += 1

            if cnt == 60:
                break

    except KeyboardInterrupt:
        pass

    pwmR.stop()
    pwmG.stop()
    pwmB.stop()


def DoorHit(pir):
    last_Gz = 0
    d = False
    data1 = 0
    data2 = 0
    data3 = 0
    data4 = 0
    data5 = 0
    data6 = 0
    data7 = 0
    data8 = 0
    data9 = 0
    data10 = 0

    gyroAngleX = 0
    gyroAngleY = 0
    gyroAngleZ = 0
    yaw = 0
    end = time.time()
    c = 0
    AccErrX = 0
    AccErrY = 0
    GyroErrX = 0
    GyroErrY = 0
    GyroErrZ = 0
    leaveLoopCnt = 0

    while (1):
        try:
            # 讀六軸資訊
            mpu = mpu6050(0x68)
            accel_data = mpu.get_accel_data()

            # 儲存當前10筆X軸acc去判斷撞擊
            data1 = data2
            data2 = data3
            data3 = data4
            data4 = data5
            data5 = data6
            data6 = data7
            data7 = data8
            data8 = data9
            data9 = data10
            data10 = accel_data['x']
            sum = data1+data2+data3+data4+data5+data6+data7+data8+data9+data10

            max_acc = max([data1, data2, data3, data4, data5,
                           data6, data7, data8, data9, data10])
            min_acc = min([data1, data2, data3, data4, data5,
                           data6, data7, data8, data9, data10])

            # print('max-min:{}'.format(max_acc-min_acc))
            # print()

            if data1 != 0 and max_acc-min_acc > 10:
                print('[INFO] The door was hit!')
                return True
            if not pir.motion_detected:
                time.sleep(0.1)
                #print('[INFO] Turn off G-sensor')
                # return False

                leaveLoopCnt += 1
                if leaveLoopCnt == 100:
                    print('[INFO] Turn off G-sensor')
                    return False

            # 計算角度
            AccX = accel_data['x']
            AccY = accel_data['y']
            AccZ = accel_data['z']

            accAngleX = (math.atan(AccY / math.sqrt(AccX**2 + AccZ**2))
                         * 180 / math.pi) + 0.8805
            accAngleY = (math.atan(-1*AccX / math.sqrt(AccY **
                                                       2 + AccZ**2)) * 180 / math.pi) - 2.3314

            start = end
            end = time.time()
            elapsed_time = (end-start)

            gyro_data = mpu.get_gyro_data()
            GyroX = gyro_data['x'] + 0.0158
            GyroY = gyro_data['y'] + 0.0040
            GyroZ = gyro_data['z'] - \
                0.4141+0.1039-0.0320-0.0077
            gyroAngleX = gyroAngleX + GyroX * elapsed_time
            gyroAngleY = gyroAngleY + GyroY * elapsed_time

            yaw = yaw + GyroZ * elapsed_time

            roll = 0.96 * gyroAngleX + 0.04 * accAngleX
            pitch = 0.96 * gyroAngleY + 0.04 * accAngleY
            # roll =  gyroAngleX
            # pitch =  gyroAngleY

            # print("Ax:{:.4f}  Ay:{:.4f}  Az:{:.4f}  Gx:{:.4f}  Gy:{:.4f}  Gz:{:.4f} ".format(AccX, AccY, AccZ, GyroX, GyroY, GyroZ))
            # print()
            # print('yaw:{:.2f} roll:{:.2f} pitch{:.2f}'.format(yaw,roll,pitch))
            # print('angle:{:.2f}'.format(-yaw))

            # 計算累加的誤差(校正用 只需GyroZ就好)
            AccErrX = AccErrX + \
                (math.atan(AccY / math.sqrt(AccX**2 + AccZ**2))
                 * 180 / math.pi)
            AccErrY = AccErrY + \
                (math.atan(-1*AccX /
                           math.sqrt(AccY**2 + AccZ**2)) * 180 / math.pi)
            GyroErrX = GyroErrX + GyroX
            GyroErrY = GyroErrY + GyroY
            GyroErrZ = GyroErrZ + GyroZ
            c = c+1
            # print(c)
            '''
            if c % 1000 == 0:
                print('AccErrX:{:.4f}, AccErrY:{:.4f}, GyroErrX:{:.4f}, GyroErrY:{:.4f}, GyroErrZ:{:.4f} '.format(
                    AccErrX/c, AccErrY/c, GyroErrX/c, GyroErrY/c, GyroErrZ/c))
            '''
        except KeyboardInterrupt:
            break

        time.sleep(0.0001)


def DoorClose_gSensor():
    last_Gz = 0
    d = False
    data1 = 0
    data2 = 0
    data3 = 0
    data4 = 0
    data5 = 0
    data6 = 0
    data7 = 0
    data8 = 0
    data9 = 0
    data10 = 0

    gyroAngleX = 0
    gyroAngleY = 0
    gyroAngleZ = 0
    yaw = 0
    end = time.time()
    c = 0
    AccErrX = 0
    AccErrY = 0
    GyroErrX = 0
    GyroErrY = 0
    GyroErrZ = 0
    openFlag = 0
    while (1):
        try:
            # 讀六軸資訊
            mpu = mpu6050(0x68)
            accel_data = mpu.get_accel_data()

            # 儲存當前10筆X軸acc去判斷撞擊
            data1 = data2
            data2 = data3
            data3 = data4
            data4 = data5
            data5 = data6
            data6 = data7
            data7 = data8
            data8 = data9
            data9 = data10
            data10 = accel_data['x']
            sum = data1+data2+data3+data4+data5+data6+data7+data8+data9+data10

            max_acc = max([data1, data2, data3, data4, data5,
                           data6, data7, data8, data9, data10])
            min_acc = min([data1, data2, data3, data4, data5,
                           data6, data7, data8, data9, data10])

            # print('max-min:{}'.format(max_acc-min_acc))
            # print()

            '''
            if data1 != 0 and max_acc-min_acc > 10:
                print('[INFO] The door was hit!')
                break
            '''

            # 計算角度
            AccX = accel_data['x']
            AccY = accel_data['y']
            AccZ = accel_data['z']

            accAngleX = (math.atan(AccY / math.sqrt(AccX**2 + AccZ**2))
                         * 180 / math.pi) + 0.8805
            accAngleY = (math.atan(-1*AccX / math.sqrt(AccY **
                                                       2 + AccZ**2)) * 180 / math.pi) - 2.3314

            start = end
            end = time.time()
            elapsed_time = (end-start)

            gyro_data = mpu.get_gyro_data()
            GyroX = gyro_data['x'] + 0.0158
            GyroY = gyro_data['y'] + 0.0040
            GyroZ = gyro_data['z'] - \
                0.4141+0.1039-0.0320-0.0077
            gyroAngleX = gyroAngleX + GyroX * elapsed_time
            gyroAngleY = gyroAngleY + GyroY * elapsed_time

            yaw = yaw + GyroZ * elapsed_time

            roll = 0.96 * gyroAngleX + 0.04 * accAngleX
            pitch = 0.96 * gyroAngleY + 0.04 * accAngleY
            # roll =  gyroAngleX
            # pitch =  gyroAngleY

            # print("Ax:{:.4f}  Ay:{:.4f}  Az:{:.4f}  Gx:{:.4f}  Gy:{:.4f}  Gz:{:.4f} ".format(AccX, AccY, AccZ, GyroX, GyroY, GyroZ))
            # print()
            # print('yaw:{:.2f} roll:{:.2f} pitch{:.2f}'.format(yaw,roll,pitch))
            # print('angle:{:.2f}'.format(-yaw))
            if (-yaw < -10 or -yaw > 10) and openFlag == 0:
                openFlag = 1
                print("[INFO] 門已開啟")

            if -yaw >= -10 and -yaw <= 10 and openFlag == 1:
                closeFlag = 1
                print("[INFO] 門已關上")
                break

            # 計算累加的誤差(校正用 只需GyroZ就好)
            AccErrX = AccErrX + \
                (math.atan(AccY / math.sqrt(AccX**2 + AccZ**2))
                 * 180 / math.pi)
            AccErrY = AccErrY + \
                (math.atan(-1*AccX /
                           math.sqrt(AccY**2 + AccZ**2)) * 180 / math.pi)
            GyroErrX = GyroErrX + GyroX
            GyroErrY = GyroErrY + GyroY
            GyroErrZ = GyroErrZ + GyroZ
            c = c+1
            # print(c)
            '''
            if c % 1000 == 0:
                print('AccErrX:{:.4f}, AccErrY:{:.4f}, GyroErrX:{:.4f}, GyroErrY:{:.4f}, GyroErrZ:{:.4f} '.format(
                    AccErrX/c, AccErrY/c, GyroErrX/c, GyroErrY/c, GyroErrZ/c))
            '''
        except KeyboardInterrupt:
            break

        time.sleep(0.0001)
