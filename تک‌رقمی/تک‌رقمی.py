n = int(input())
count = 0
while n>=10:
	count = 0
	while n>0:
		count = count + (n%10)
		n = n // 10
	n = count
print(n)