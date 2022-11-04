from djitellopy import Tello
import cv2
import numpy as np
import pygame


def intializeTello():
    # CONNECT TO TELLO
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 0
    myDrone.yaw_velocity = 0
    myDrone.speed =0
    #print(myDrone.get_battery())
    #myDrone.streamoff()
    #myDrone.streamon()
    return myDrone

def telloGetFrame(myDrone,w=360,h=240):
    # GET THE IMGAE FROM TELLO
    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w, h))
    return img

def findFace(img):
    # faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)
    myFaceListC = []
    myFaceListArea = []
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cx = x + w // 2
        cy = y + h // 2
        area = w * h
        cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
        myFaceListC.append([cx, cy])
        myFaceListArea.append(area)

    if len(myFaceListArea) != 0:
        i = myFaceListArea.index(max(myFaceListArea))
        return img, [myFaceListC[i], myFaceListArea[i]]
    else:
        return img, [[0, 0], 0]

# def trackFace(myDrone,c,w,pid,pError):
#     print(c)
#     error = c[0][0] - w//2
#     # Current Value - Target Value
#     speed = int(pid[0]*error + pid[1] * (error-pError))
#     if c[0][0] != 0:
#         myDrone.yaw_velocity = speed
#     else:
#         myDrone.left_right_velocity = 0
#         myDrone.for_back_velocity = 0
#         myDrone.up_down_velocity = 0
#         myDrone.yaw_velocity = 0
#         error = 0
# # SEND VELOCITY VALUES TO TELLO
#     if myDrone.send_rc_control:
#         myDrone.send_rc_control(myDrone.left_right_velocity, myDrone.for_back_velocity,
#         myDrone.up_down_velocity, myDrone.yaw_velocity)
#     return error

def trackFace(myDrone, info, w, h, pid, pError):
    print(info)
    fbRange = [3200, 6800]
    area = info[1]
    x, y = info[0]
    print("x: " + str(x))
    print("y: " + str(y))
    print("pid[0]: " + str(pid[0]))
    print("pid[1]: " + str(pid[1]))

    fb = 0
    error = x - w // 2
    errorHeight = y + h //2
    print("errorHeight: " + str(errorHeight))
    rotationSpeed = pid[0] * error + pid[1] * (error - pError)
    rotationSpeed = int(np.clip(rotationSpeed, -100, 100))
    heightSpeed = pid[0] * error + pid[1] * (errorHeight - pError)
    heightSpeed = int(np.clip(heightSpeed, -20, 20))
    print("heightSpeed: " + str(heightSpeed))

    if area > fbRange[0] and area < fbRange[1]:
        fb = 0
    elif area > fbRange[1]:
        fb = -20
    elif area < fbRange[0] and area != 0:
        fb = 20
    if x == 0:
        rotationSpeed = 0
        heightSpeed = 0
        error = 0
    # print(speed, fb)
    #myDrone.send_rc_control(0, fb, 0, rotationSpeed)
    myDrone.send_rc_control(0, fb, heightSpeed, rotationSpeed)
    return error


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans