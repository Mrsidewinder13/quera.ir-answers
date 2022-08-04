a=float(input())
b=float(input())
c=float(input())
delta = (b*b)-(4*a*c)
if(a==0 and b==0):
    print("IMPOSSIBLE")
elif(a==0):
    print("{:.3f}".format(-c/b))
elif(delta>0):
    delta=delta**.5
    x1=(-b-delta)/(2*a)
    x2=(-b+delta)/(2*a)
    print("{:.3f}".format(x1))
    print("{:.3f}".format(x2))
elif(delta==0):

    print("{:.3f}".format(c**.5))
else:
    print("IMPOSSIBLE")