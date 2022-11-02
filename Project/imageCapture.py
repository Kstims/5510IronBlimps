from djitellopy import tello
import cv2
import KeyPressModule as kp
from time import sleep

me = tello.Tello()
me.connect()
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Image", img)
    cv2.waitkey(1)

def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0,
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

me.takeoff()