x = input().split()
count = 0
for i in x:
    if int(i) >= 80:
        count += 1
if count >= 3:
    print('Mamma mia!')
elif 1 <=count <=2:
    print('Mamma mia!!')
else:
    print('Mamma mia!!!')