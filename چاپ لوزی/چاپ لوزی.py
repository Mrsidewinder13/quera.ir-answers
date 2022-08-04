n = int(input())
number = 0
i = 0
while i <= 2*n+1:
    if i < n:
        print(' '* (n-i), end='')
        print('*' * (2 * i +1),end='')
    else:
        print(' ' * (i-n), end='')
        print('*' * (4 * n - 2 * i + 1 ), end='')
    i += 1
    print()