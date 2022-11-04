from djitellopy import Tello
import cv2
import faceTrackUtil as ftu
import time

myDrone = ftu.intializeTello()
print("Battery level: " + str(myDrone.get_battery()))
myDrone.streamon()
time.sleep(5)
myDrone.takeoff()
#myDrone.send_rc_control(0, 0, 20, 0)
#time.sleep(10)
#myDrone.send_rc_control(0, 0, 0, 0)
#time.sleep(2.2)
w, h = 480, 360
pid = [0.4, 0.4, 0]
pError = 0

while True:
    # _, img = cap.read()
    img = myDrone.get_frame_read().frame
    img = cv2.resize(img, (w, h))
    img, info = ftu.findFace(img)
    pError = ftu.trackFace(myDrone,info,w, h, pid,pError)
    # print("Center", info[0], "Area", info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        myDrone.streamoff()
        myDrone.land()
        myDrone.end()
        break
