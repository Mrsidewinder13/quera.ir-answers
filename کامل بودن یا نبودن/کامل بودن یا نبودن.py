# solution 1
# number = int(input())
# count = 0
# for i in range(1,number):
#     if number%i ==0:
#         count += i
# if (count == number):
#     print('YES')
# else:
#     print('NO')


# solution 2
number = int(input())
count = 0
i = 0
while i < (number-1):
    i += 1
    if number %i == 0:
        count += i
if (count == number):
    print('YES')
else:
    print('NO')