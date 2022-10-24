from math import cos, sin, radians, degrees, sqrt, atan2
import random

max_float = radians(360)

d1 = 0          #can be set to anything, just affects z
d2 = 0.5
d3 = 1.0
d6 = 0.2        #constant

x_goal = 1.2
y_goal = 0.8
z_goal = 0.5

n = 10000

t1 = radians(-90)
t4 = radians(-90)
t5 = radians(90)
t6 = radians(40)       #does not affect solution
threshold = 0.1

x = (cos(t1) * cos(t4) * sin(t5) * d6) - (sin(t1) * cos(t5) * d6) - (sin(t1) * d3)
y = (sin(t1) * cos(t4) * sin(t5) * d6) + (cos(t1) * cos(t5) * d6) + (cos(t1) * d3)
z = 0 - (sin(t4) * sin(t5) * d6) + d1 + d2

print("Start x, y, z: {:.2f}, {:.2f}, {:.2f}".format(x,y,z))


def dist(x1, x2, y1, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

for i in range(n):
    t1_diff = ((random.random()-.5) * .3) * max_float
    t4_diff = ((random.random()-.5) * .3) * max_float
    t5_diff = ((random.random()-.5) * .3) * max_float
    t1_tmp = t1 + t1_diff
    t4_tmp = t4 + t4_diff
    t5_tmp = t5 + t5_diff
    
    #x_tmp = (cos(t1_tmp) * cos(t4_tmp) * sin(t5_tmp) * d6) - (sin(t1_tmp) * cos(t5_tmp) * d6) - (sin(t1_tmp) * d3)
    #y_tmp = (sin(t1_tmp) * cos(t4_tmp) * sin(t5_tmp) * d6) + (cos(t1_tmp) * cos(t5_tmp) * d6) + (cos(t1_tmp) * d3)
    #z_tmp = 0 - (sin(t4_tmp) * sin(t5_tmp) * d6) + d1 + d2

    x_tmp = cos(t4_tmp) * sin(t5_tmp) * d6
    y_tmp = sin(t4_tmp) * sin(t5_tmp) * d6
    z_tmp = cos(t5_tmp) * d6
    #print("x, y, z: {:.2f}, {:.2f}, {:.2f}".format(x_temp,y_temp,z_temp))
    
    if abs(x - x_goal) < threshold and abs(y - y_goal) < threshold:
        print("success")
        print("Final XYZ {} {} {}".format(x,y,z))
        print("Final thetas {} {} {}".format(t1_tmp, t4_tmp, t5_tmp))
        print("num iter {}".format(i))
        break
        
    curDist = dist(x_goal, x, y_goal, y)
    tempDist = dist(x_goal, x_tmp, y_goal, y_tmp)
    
    #print("cur temp {:.2f} {:.2f}".format(curDist,tempDist))
    
    if curDist < tempDist:
        pass
    else:
        t1 = t1_tmp
        t4 = t4_tmp
        t5 = t5_tmp
        x = x_tmp
        y = y_tmp
        z = z_tmp
        
print("x, y, z: {:.6f}, {:.6f}, {:.6f}".format(x,y,z))
