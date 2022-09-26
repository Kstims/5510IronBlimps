import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')


# Creates the list of commands for the bot to follow every tick
def generateCommands(interval, turn):
    commandList = []

    print("interval =" + str(interval))
    for x in range(int(10 / interval)):
        commandList.append((interval, turn))

    return commandList


# Runs the list of commands to move the bot
def runCommands(kList):
    time = 0
    xNot = -2.5
    yNot = 0
    theta = 0
    xCoord = [xNot]
    yCoord = [yNot]
    xPoint = [xNot]
    yPoint = [yNot]
    xVels = []
    yVels = []
    angVels = []
    times = []

    for x in range(0, len(kList)):
        xNot, yNot, theta, angVel, xV, yV = kinematics(xNot, yNot, theta, kList[x][1], kList[0][0])
        xCoord.append(xNot)
        yCoord.append(yNot)
        xVels.append(xV)
        yVels.append(yV)
        angVels.append(angVel)
        time += kList[0][0]
        times.append(time)
        # print("Position: (" + str(xNot) + ", " + str(yNot) + ") theta = " + str(theta))
        # print("Trajectory: (" + str(xV) + ", " + str(yV) + ") Angular Velocity = " + str(angVel))
        # print("At T = " + str(time))
        xPoint.append(xNot)
        yPoint.append(yNot)

    plotCharts(xCoord, yCoord, xPoint, yPoint, xVels, yVels, angVels, times, kList[0][0])


# calculates position and velocities
def kinematics(x, y, theta, alpha, tInterval):
    LENGTH = .75
    VELOCITY = 8

    xNew = x - VELOCITY * np.sin(theta) * tInterval
    yNew = y + VELOCITY * np.cos(theta) * tInterval
    thetaNew = theta + (VELOCITY / LENGTH) * np.tan(alpha) * tInterval
    aVel = (VELOCITY / LENGTH) * np.tan(alpha)
    xVel = -1 * VELOCITY * np.sin(theta)
    yVel = VELOCITY * np.cos(theta)
    return xNew, yNew, thetaNew, aVel, xVel, yVel


# draws the figures
def plotCharts(xCoordinate, yCoordinate, xPos, yPos, xVelocity, yVelocity, aVelocity, tList, deltaT):
    figure, ax = plt.subplots(2, 2, tight_layout=True, figsize=(6, 6))
    Drawing_uncolored_circle = plt.Circle((0, 0),
                                          2.5,
                                          fill=False)
    ax[0, 0].add_artist(Drawing_uncolored_circle)
    ax[0, 0].set_aspect(1)
    if (deltaT > .1):
        ax[0, 0].set(xlim=(-10, 10), ylim=(-10, 10))
    else:
        ax[0, 0].set(xlim=(-3, 3), ylim=(-3, 3))

    ax[0, 0].plot(xPos, yPos, linewidth=2, marker='.')
    ax[0, 0].set_title("Question 1c: " + 'Delta: \u0394' + "t= " + str(deltaT))

    ax[0, 1].set_xlabel('t (seconds)')
    ax[0, 1].set_ylabel('x velocity (m/s)')
    ax[0, 1].plot(tList, xVelocity)
    ax[0, 1].set_title("X Velocity over time")

    ax[1, 0].set_xlabel('t (seconds)')
    ax[1, 0].set_ylabel('y velocity (m/s)')
    ax[1, 0].plot(tList, yVelocity)
    ax[1, 0].set_title("Y Velocity over time")

    ax[1, 1].set_xlabel('t (seconds)')
    ax[1, 1].set_ylabel('theta velocity (m/s)')
    ax[1, 1].plot(tList, aVelocity)
    ax[1, 1].set_title("Angular Velocity over time")

    plt.show(block=False)


# runs the program using different delta-Ts
dt = [.1, .01, 1]

# main driver
for x in range(len(dt)):
    commandListing = generateCommands(dt[x], -.291457)
    runCommands(commandListing)
plt.show()
