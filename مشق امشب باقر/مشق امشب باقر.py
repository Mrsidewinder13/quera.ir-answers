a, b , c = input().split()
a = int(a)
b = int(b)
c = int(c)
if a+b+c==180 and 0 < a and 0 < b and 0 < c:
    print('Yes')
else:
    print('No')