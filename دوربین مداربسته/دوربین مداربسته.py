x1,y1 = input().split()
x2,y2 = input().split()
x3,y3 = input().split()
x4 = 0
y4 = 0
if int(x1) == int(x2):
	x4 = x3
elif int(x1) == int(x3):
	x4 = x2
else:
	x4 = x1
if int(y1) == int(y2):
	y4 = y3
elif int(y1) == int(y3):
	y4 = y2
else:
	y4 = y1
print(x4,y4)