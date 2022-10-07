import math

t1 = math.radians(-90)
t4 = math.radians(-90)
t5 = math.radians(90)
t6 = math.radians(40)       #does not affect solution

d1 = 0          #can be set to anything
d2 = 0.5
d3 = 1.0
d6 = 0.2        #constant

endx = 1.2
endy = 0.8
endz = 0.5

dx = (math.cos(t1) * math.cos(t4) * math.sin(t5) * d6) - (math.sin(t1) * math.cos(t5) * d6) - (math.sin(t1) * d3)

dy = (math.sin(t1) * math.cos(t4) * math.sin(t5) * d6) + (math.cos(t1) * math.cos(t5) * d6) + (math.cos(t1) * d3)

dz = 0 - (math.sin(t4) * math.sin(t5) * d6) + d1 + d2

print("x: {:.2f}\n".format(dx))
print("y: {:.2f}\n".format(dy))
print("z: {:.2f}\n".format(dz))
