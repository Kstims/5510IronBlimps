import math





#calculate angular accelleration
def theta_acc(length, force, mass_pole, mass_cart, theta, theta_dot):
    top = 9.8*math.sin(theta) + math.cos(theta)*((-1*force - mass_pole*length*(theta_dot**2)*math.sin(theta)) / (mass_cart + mass_pole))
    bottom = length*((4/3) - ((mass_pole*(math.cos(theta)**2)) / (mass_cart + mass_pole)))
    return top / bottom

#calculate cart accelleration
def x_acc(length, force, mass_pole, mass_cart, theta, theta_dot, theta_acc):
    return (force + mass_pole*length*((theta_dot**2)*math.sin(theta) - theta_acc*math.cos(theta))) / (mass_cart + mass_pole)

def radToDegrees(theta):
    return math.pi * theta / 180

def trunc(values, decs = 0):
    return math.trunc(values*10**decs)/(10**decs)

#thetaAcc = thetaDoubleDot = accelleration
#thetaDot = thetaDot = velocity
#tau = DT = time interval
massPole = 0.2
massCart = 4.0
length = 1.0
force = 0.0
tau = 0.01
theta = math.pi / 24
thetaVelocity = 0
xVelocity = 0
#distance from the center
x = 0
t = 0

#main driver

print("Starting position theta = " + str(theta) + ", " + str(radToDegrees(theta)) + " degrees" + " Pos = " + str(x))

while True:
    #thetaAccNew = theta_acc(length, force, massPole, massCart, theta, thetaVelocity)
    #xAccNew = x_acc(length, force, massPole, massCart, theta, thetaVelocity, thetaAccNew)
    if (force != 0 ):
        input()
    tmp = (
                  force + length * thetaVelocity ** 2 * math.sin(theta)
          ) / (massCart + massPole)
    thetaAccNew = (9.8 * math.sin(theta) - math.cos(theta) * tmp) / (
            length * (4.0 / 3.0 - massPole * math.cos(theta) ** 2 / (massCart + massPole))
        )
    xAccNew = tmp - length * thetaAccNew * math.cos(theta) / (massCart + massPole)

    thetaVelocity += thetaAccNew * tau
    thetaOld = theta
    theta += thetaVelocity * tau
    xVelocity += xAccNew
    x += xVelocity * tau

    #determining if pole is to the left (-theta) or right (+theta)
    #pole to the left
    if theta < 0:
        #flag if pole just passed apogee
        if thetaOld >= 0:
            #reversing force and decreasing by half
            force = -1 * abs(force/2)
            if force == 0:
                force = -2
            print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
        else:
            #increasing force by 1%
            # force = -1 * abs(force*1.01)
            # if force == 0:
            #     force = -2
            # if force > 10:
            #     force = 10
            print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
    #pole to the right
    elif theta > 0:
        if thetaOld <= 0:
            force = abs(force/2)
            if force == 0:
                force = 2
            print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
        else:
            # force = abs(force*1.01)
            # if force == 0:
            #     force = 2
            # if force > 10:
            #     force = 10
            print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
    #pole is in perfect center. Stopping cart
    else:
        force = 0
        print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
    t += tau
    #Failure to balance if the pole has dropped below horizon (theta > 90 or theta < -90
    if theta < -90 or theta > 90:
        print("Failure to balance at T = " + str(t))
        print("Theta: " + str(theta) + ", " + str(radToDegrees(theta)) + "degrees. Force: " + str(force) + " Pos = " + str(x))
        break

