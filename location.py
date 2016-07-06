ndegree=0

ndegree=float(raw_input("the present degree"))

j=ndegree%360
a=ndegree-j
k=ndegree/a
newdegree=(k*ndegree+degree)
if round(degree,0) in range(0,45):
	a="East"
	print (a,degree)
elif round(degree,0) in range(315,360):
	a="East"
	print (a,degree)
elif round(degree,0) in range(45,135):
	a="North"
	print (a,degree)
elif round(degree,0) in range(135,225):
	a="West"
	print (a,degree)
elif round(degree,0) in range(225,315):
	a="South"
	print (a,degree)
