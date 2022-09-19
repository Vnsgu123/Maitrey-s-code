try:
    # cook your dish here
    t=int(input())
    # n=int(input())
    
    def ADD(z,items):
        u=z.split()
        u[2]=int(u[2])
        flag =0
        for i in range(0,len(items)):
            if u[1]==items[i][0]:
                flag=1
                items[i][1]=items[i][1]+u[2]
                print("UPDATED Item ",u[1])
        if flag == 0:
            u[2]=str(u[2])
            l=u[1]+" "+u[2]
            # print(l)
            # k=l.split()
            items.append(l)
            # k[1]=int(k[1])
            print("ADDED Item ",u[1])
            
    def DELETE(z,items):
        u=z.split()
        flag=0
        u[2]=int(u[2])
        for i in range(0,len(items)):
            if u[1]==items[i][0]:
                flag=1
                items[i][1]=int(items[i][1])
                if u[2] <= items[i][1] :
                    items[i][1]=items[i][1]-u[2]
                    print("DELETED Item ",u[1])
                # elif u[2]==items[i][1]:
                #     items.remove(items[i])
                #     print("DELETED Item ",u[1])
                else :
                    print("Item "+ u[1] + " could not be DELETED")
        if flag == 0 :
            print("Item " + u[1] +" does not exist")   
         
    def SUM(items):
        sum = 0
        for i in range(0,len(items)):
            sum = sum + items[i][1]
        print("Total Items in Inventory:",sum)           
    
    while t:
        n=int(input())
        # n=int(input())
        items = []
        for i in range(0,n):
            x = input()
            y = x.split()
            # y[1]=int(y[1])
            items.append(y)
        # print(items)
        m=int(input())
        for j in range(0,m):
            z=input()
            h=z.split()
            if h[0]=="ADD" :
                ADD(z,items)
            if h[0]=="DELETE":
                DELETE(z,items)
        SUM(items)
except EOFError as e:
    pass
