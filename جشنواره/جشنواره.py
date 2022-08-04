x = int(input())
out = 0
for i in range(2,x):
    if x % i == 0:
        out = i
if out == 0:
    print(1)
else:
    print (out)