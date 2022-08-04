n = int(input())
x = 0
y = 0
for i in range(2,n+1):
    b = i%4
    if i%4 ==2:
        x = -x+1
    elif i%4 == 3:
        y = -y + 1
    elif i%4 == 0:
        x = -x
    elif i%4 == 1:
        y = -y
print(x,y)