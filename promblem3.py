t=int(input())

while t:
    n=int(input())
    for i in range(n,0,-1):
        for j in range(1,i+1):
            if j%5==0:
                print("#",end="")
            else:
                print("*",end="")
        print("")
    t=t-1    