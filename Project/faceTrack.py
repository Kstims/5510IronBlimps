from djitellopy import Tello
import cv2
import faceTrackUtil as ftu
import time
import math


# Makes connection between drone and computer, activates camera, and lifts off
droneFly = True
myDrone = ftu.intializeTello()
print("Battery level: " + str(myDrone.get_battery()))
myDrone.streamon()
time.sleep(5)
if droneFly:
    myDrone.takeoff()
myDrone.send_rc_control(0, 0, 10, 0)
time.sleep(10)
myDrone.send_rc_control(0, 0, 0, 0)
time.sleep(2.2)
w, h = 480, 360
pid = [0.4, 0.4, 0]
pError = 0

tracker = cv2.legacy.TrackerMOSSE_create()
makeBox = True
boxMade = False
fail_count = 0
bbox = None
ok = None
fps = 0

# Main loop
while True:
    # _, img = cap.read()
    # receives image from camera feed
    img = myDrone.get_frame_read().frame

    # resizes image to set width/height
    img = cv2.resize(img, (w, h))
    # detects face in frame

    myDrone.get_battery()
    img, info = ftu.findFace(img)
    # Create bounding box
    # makeBox = True
    if makeBox:
        if info[1] != 0:
            side = int(math.sqrt(info[1]))
            x, y = info[0]
            bbox = (int(x-(side/2)), int(y-(side/2)), side, side)
            _, _, w1, h1 = bbox
            ratio = w1/h1
            # Initialize tracker with first frame and bounding box
            tracker = cv2.legacy.TrackerMOSSE_create()
            ok = tracker.init(img, bbox)
            makeBox = False
            fail_count = 0
            boxMade = True
   

    #Update tracker
    if bbox is not None:
        timer = cv2.getTickCount()
        x0, y0, w0, h0 = bbox
        prior_x = x0 + w0//2
        prior_y = y0 + h0//2
        area1 = w0*h0
        ok, bbox = tracker.update(img)
        x1, y1, w1, h1 = bbox
        if info[1] != 0:
            side = int(math.sqrt(info[1]))
            faceX, faceY = info[0]
            faceBbox = (int(faceX-(side/2)), int(faceY-(side/2)), side, side)
            if faceX > x1 and faceX < x1 + w1 and faceY > y1 and faceY < y1 + h1:
                tracker = cv2.legacy.TrackerMOSSE_create()
                ok = tracker.init(img, bbox)
        
        
        next_x = x1 + w1 // 2
        next_y = y1 + h1 // 2
        area2 = w1*h1
        box_diff = math.sqrt((x1-x0)**2 + (y1-y0)**2)
        # if not boxMade and (box_diff > 40 or 0.9 < (area1/area2) < 1.1):
        #     ok = False
        #     makeBox = True
        #     boxMade = False
        if h1 == 0 or w1/h1 > ratio * 1.25 or w1/h1 < ratio / 1.25:
            ok = False
            makeBox = True
            boxMade = False
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    if info[1] != 0:
        x, y = info[0]
        faceBBox = (int(x-(side/2)), int(y-(side/2)), side, side)
        p1 = (int(faceBBox[0]), int(faceBBox[1]))
        p2 = (int(faceBBox[0] + faceBBox[2]), int(faceBBox[1] + faceBBox[3]))
        cv2.rectangle(img, p1, p2, (0, 255, 0), 2, 1)
    # tracts face coordinates in frame to determine movement
    if ok is not None and ok:
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(img, p1, p2, (255, 0, 0), 2, 1)

        # Use drone moving function based on object tracking
        x1, y1 = p1
        x2, y2 = p2
        width, height = x2-x1, y2-y1
        cx = x1 + width // 2
        cy = y1 + height // 2
        area = width * height
        info = [[cx, cy], area]
        pError = ftu.trackFace(myDrone, info, w, h, pid, pError)
    else:
        # Tracking failure
        fail_count += 1
        if fail_count > 60:  # If the tracking failed for long enough, try to reset it.
            makeBox = True
        cv2.putText(img, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display tracker type and fps on img
    cv2.putText(img, "CSRT Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
    cv2.putText(img, "FPS : " + str(int(fps)), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)

    # print("Center", info[0], "Area", info[1])
    # displays image
    cv2.imshow("Output", img)

    # press 'q' to land drone and shutdown
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        myDrone.streamoff()
        if droneFly:
            myDrone.land()
        break
