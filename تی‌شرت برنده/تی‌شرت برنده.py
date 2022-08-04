x1,y1 = [int(x) for x in input().split()]
x2,y2 = [int(x) for x in input().split()]
while 1<= x1 and y1 and x1 and x2<= 100:
	if x1 >= x2 and y1 >= y2:
		print('yes')
		break
	else:
		print('no')
		break