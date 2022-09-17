t=input()
t=int(t)

    for i in range(0,2):
        m[i]=input()
    for i in t:
        if(m[i]==0):
            print("3")
        elif m[i]%2==0:
            m[i]=m[i]*2
            print(m[i])
        else:
            m[i]=m[i]*m[i]
            print(m[i])
            