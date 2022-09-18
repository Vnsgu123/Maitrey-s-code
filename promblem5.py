t=int(input())

while t:
    n=int(input())
    num=[]
    x=input()
    y=x.split()
    for i in range (0,n):
        y[i]=int(y[i])
    num.append(y)
    # print(y)
    y.reverse()
    z=str(y)
    z=z.replace(',',' ')
    print(z)
    y.reverse()
    # print(y)
    # print(y[3::3])
    k=y[3::3]
    for j in range(0,len(k)):
        k[j]=k[j]+3
    # print(k)
    q=str(k)
    q=q.replace(',',' ')
    print(q)
    l=y[5::5]
    for p in range(0,len(l)):
        l[p]=l[p]-7
    # print(l)
    w=str(l)
    w=w.replace(',',' ')
    print(l)
    f=y[3:7]
    sum =0
    for t in range(0,len(f)):
        sum = sum + f[t]
    print(sum)
    