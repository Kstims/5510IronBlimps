from djitellopy import Tello
import cv2
import faceTrackUtil as ftu
import time


# Makes connection between drone and computer, activates camera, and lifts off
droneFly = False
myDrone = ftu.intializeTello()
print("Battery level: " + str(myDrone.get_battery()))
myDrone.streamon()
time.sleep(5)
if (droneFly):
    myDrone.takeoff()
# myDrone.send_rc_control(0, 0, 20, 0)
# time.sleep(10)
# myDrone.send_rc_control(0, 0, 0, 0)
# time.sleep(2.2)
w, h = 480, 360
pid = [0.4, 0.4, 0]
pError = 0

# Main loop
while True:
    # _, img = cap.read()
    # receives image from camera feed
    img = myDrone.get_frame_read().frame
    # resizes image to set width/height
    img = cv2.resize(img, (w, h))
    # detects face in frame
    img, info = ftu.findFace(img)
    # tracts face coordinates in frame to determine movement
    pError = ftu.trackFace(myDrone, info, w, h, pid, pError)
    # print("Center", info[0], "Area", info[1])
    # displays image
    cv2.imshow("Output", img)

    # press 'q' to land drone and shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        myDrone.streamoff()
        if (droneFly):
            myDrone.land()
        myDrone.end()
        print("Drone disengaged")
        break
