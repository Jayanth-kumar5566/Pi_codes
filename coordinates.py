#This program converts radial coordinates to catrisean and vice-versa
import math
print"What do you want to do'\n'1.cartesian to polar'\n'2.polar to cartesian "                                                                                                        
a=int(raw_input("Give me the option "))
if a==1:
	x=float(raw_input("Please enter the x cartesian value"))
	y=float(raw_input("Please enter the y cartesian value"))
	r=(x**2+y**2)**0.5
	o=math.atan(y/x)
	theta=math.degrees(o)
	print (r,theta)

else:
	r=float(raw_input("Please enter the radius"))
	theta=float(raw_input("Please enter the angle"))
	o=math.radians(theta)
	x=math.cos(o)*r
	y=math.sin(o)*r
	print(x,y)