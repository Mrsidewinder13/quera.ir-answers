n = int(input())
n = n//2+1
i = 0
while i<n:
    print(' ' * (n-i-1) + '*'*(i+(i+1)) + '  ' * (n-i-1)+'*'*(i+(i+1)))
    i+=1
j = n-1
while j>0: 
    print(' '*(n-j)+'*'*(j*2-1)+'  '*(n-j)+'*'*(j*2-1))
    j-=1
