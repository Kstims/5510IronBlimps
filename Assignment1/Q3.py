import math
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')







def kinematics(l, r, W, x, y, theta, DT):
    xNew = x - .5 * (l + r) * np.sin(theta) * DT
    yNew = y + .5 * (l + r) * np.cos(theta) * DT
    thetaNew = theta + (1 / W) * (r - l) * DT
    aVel = (thetaNew - theta) / DT
    xVel, yVel = getVelocity(x, y, xNew, yNew, DT)
    return xNew, yNew, thetaNew, aVel, xVel, yVel

def strafe(l, r, x, y, theta, DT):

    #strafe right
    if l < r:
        velocity = abs(r) * DT

    # strafe left
    else:
        velocity = l * dt

    yNew = velocity * np.sin(theta) + y
    xNew =  velocity * np.cos(theta) + x
    xVel, yVel = getVelocity(x, y, xNew, yNew, DT)
    return xNew, yNew, xVel, yVel

def getVelocity(x0, y0, x1, y1, DT):
    distance = np.sqrt(np.square(x1 - x0) + np.square(y1 - y0))
    velocity = distance / DT
    magX = x1-x0
    magY = y1-y0
    if magX == 0:
        if magY > 0:
            thetaDegrees = 90
        else:
            thetaDegrees = 180
    else:
        thetaDegrees = np.arctan(magY / magX)
    yVel = velocity * np.sin(thetaDegrees)
    xVel = velocity * np.cos(thetaDegrees)
    if np.isnan(yVel):
        yVel = 0
    if np.isnan(xVel):
        xVel = 0
    print("")
    return xVel, yVel


WIDTH = .3
DT = .1
time = 0
xNot = .15
yNot = 0
theta = 0
xCoord = [xNot]
yCoord = [yNot]
xPoint = [xNot]
yPoint = [yNot]

# (1, .23562, -.23562) = 90 degree clockwise turn
# (1, -.23562, .23562) = 90 degree counterclockwise turn
kList = [(5, 1, 1, 0), #movement forward sequence
         (1, -.3, .3, 1), #strafe right sequence
         (5, -1, -1, 0), #movement backward sequence
         (1, -.3, .3, 1)] #strafe right sequence




print("(" + str(xNot) + ", " + str(yNot) + ") theta= " + str(theta))
print("At T = " + str(time))
for z in range(0, 9):
    for x in range(0, len(kList)):
        for y in range(0, kList[x][0] * 10):
            if(kList[x][3] == 0):
                xNot, yNot, theta, angVel, xV, yV = kinematics(kList[x][1], kList[x][2], WIDTH, xNot, yNot, theta, DT)
            else:
                xNot, yNot, xV, yV = strafe(kList[x][1], kList[x][2], xNot, yNot, theta, DT)
                angVel = 0
            xCoord.append(xNot)
            yCoord.append(yNot)
            time += .1
            print("Position: (" + str(xNot) + ", " + str(yNot) + ")")
            print("Trajectory: (" + str(xV) + ", " + str(yV) + ") Angular Velocity = " + str(angVel))
            print("At T = " + str(time))
        xPoint.append(xNot)
        yPoint.append(yNot)








fig, ax = plt.subplots(constrained_layout=True, figsize = (6, 6))
ax.step(xCoord, yCoord)
ax.set_xlabel('x (meters)')
ax.set_ylabel('y (meters)')
plt.title("Question 3: Swedish wheel coverage of 5x5 plot")
plt.plot(xPoint, yPoint, linewidth = 2, marker = '.')
plt.show()