x,y,x1,y1 = input().split()
if int(y) == int(y1):
	print('Horizontal')
elif int(x) == int(x1):
	print('Vertical')
else:
	print('Try again')