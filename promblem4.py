import math
t=input()
t=int(t)

while t:
    a=input()
    a=int(a)
    b=input()
    b=int(b)
    c=input()
    c=int(c)
    d=input()
    d=int(d)
    x=(a-c)*(a-c)
    y=(b-d)*(b-d)
    z=x+y
    z=math.sqrt(z)
    print(z)
    t=t-1