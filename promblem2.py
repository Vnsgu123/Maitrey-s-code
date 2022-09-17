t=input()
t=int(t)

while t:
    n=int(input())
    
    for i in range(0,n):
        if i==0:
            print(i+3 )
        elif i%2==0:
            print(i*2 )
        else:
            print(i*i )
    
    t=t-1
        