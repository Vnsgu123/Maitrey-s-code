# cook your dish here
t=int(input())

try:
        
    while t:
        n=int(input())
        students = []
        for i in range(0,n):
            y = input()
            student= y.split()
            # x  = [input() , int(input())]
            students.append(student)
        
        # print(students)
        max =students[0][1]
        name =students[0][0]
        for j in range(0,n):
            if students[j][1] > max:
               max = students[j][1]
               name = students[j][0]
        names=[]
        for p in range(0,n):
            if students[p][1] == max:
                names.append(students[p][0])
                # print(students[p][0])
        names.sort()
        for u in range(0,len(names)):
            print(names[u])
        # print(names)
except EOFError as e:
    pass
    
    # print(students)
    # print(ma
