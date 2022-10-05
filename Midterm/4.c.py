import math


def theta_acc(length, force, mass_pole, mass_cart, theta, theta_dot):
    top = 9.8*math.sin(theta) + math.cos(theta)*((-1*force - mass_pole*length*(theta_dot**2)*math.sin(theta)) / (mass_cart + mass_pole))
    bottom = length*((4/3) - ((mass_pole*(math.cos(theta)**2)) / (mass_cart + mass_pole)))
    return top / bottom


def x_acc(length, force, mass_pole, mass_cart, theta, theta_dot, theta_acc):
    return (force + mass_pole*length*((theta_dot**2)*math.sin(theta) - theta_acc*math.cos(theta))) / (mass_cart + mass_pole)




mass_pole = 0.2
mass_cart = 4.0
length = 1.0
max_force = 6.0
force = 0.0
tau = 0.01
theta = math.pi / 24
theta_dot = 0
last_theta = theta
x = 0
x_dot = 0
t = 5

#thetaAcc = thetaDoubleDot = accelleration
#thetaDot = thetaDot = velocity
#tau = DT = time interval

while True:
    curr_theta_acc = theta_acc(length, max_force, mass_pole, mass_cart, theta, theta_dot)
    curr_x_acc = x_acc(length, max_force, mass_pole, mass_cart, theta, theta_dot, curr_theta_acc)

    theta_dot += curr_theta_acc * tau
    last_theta = theta
    theta += theta_dot * tau
    x_dot += curr_x_acc
    x += x_dot * tau
    if last_theta > theta:
        print("Pushed Weight to middle from " + str(last_theta) + " to " + str(theta) + "("+str(last_theta-theta)+")" )
        theta = last_theta + (last_theta-theta)
    else:
        print("theta increased by " + str(theta-last_theta) + " test failed. Max recoverable angle is " +
              str(last_theta))
        break
print("Exited while loop")
print("unrecoverable angle = " + str(last_theta))
print("Unrecoverable angle (degrees) = " + str(last_theta*180/math.pi ))


# while t > 0 and math.pi / 2 > theta > -1 * math.pi / 2:
#     #calculate the accellerations for theta and x
#     curr_theta_acc = theta_acc(length, force, mass_pole, mass_cart, theta, theta_dot)
#     curr_x_acc = x_acc(length, force, mass_pole, mass_cart, theta, theta_dot, curr_theta_acc)
#
#     theta_dot += curr_theta_acc*tau
#     last_theta = theta
#     theta += theta_dot*tau
#     degree = radToDegree(theta)
#     print("theta = " + str(theta))
#     print("degree = " + str(degree))
#     print("force = " + str(force))
#     x_dot += curr_x_acc
#     x += x_dot * tau
#
#     # Basic control
#     if theta < 0 and theta < last_theta:
#         force = -1*max_force
#     elif theta > 0 and theta > last_theta:
#         force = max_force
#     t -= tau
