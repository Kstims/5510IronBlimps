import matplotlib.pyplot as plt
import numpy as np
plt.style.use('_mpl-gallery')

def kinematics(l, r, W, x, y, theta, DT):
    xNew = x - .5 * (l + r) * np.sin(theta) * DT
    yNew = y + .5 * (l + r) * np.cos(theta) * DT
    thetaNew = theta + (1 / W) * (r - l) * DT
    aVel = (1 / W) * (r - l)
    xVel = -.5 * (l + r) * np.sin(theta)
    yVel = .5 * (l + r) * np.cos(theta)
    return xNew, yNew, thetaNew, aVel, xVel, yVel

WIDTH = .55
LENGTH = .75
VELOCITY = 8
DIAMETER = 5
DT = .1
time = 0
xNot = 3
yNot = 3
theta = 0
xCoord = []
yCoord = []
xPoint = []
yPoint = []
xVels = []
yVels = []
angVels = []
times = []

figure, ax = plt.subplots(tight_layout=True, figsize=(6, 6))
Drawing_uncolored_circle = plt.Circle((3, 3),
                                      2.5,
                                      fill=False)
ax.set_aspect(1)
ax.add_artist(Drawing_uncolored_circle)
ax.set(xlim=(0, 6), ylim=(0, 6))
plt.title('Question 1: Skid Steer On A Circle')
plt.show()