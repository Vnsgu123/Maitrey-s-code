t=int(input())

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
    
    # print(students)
    # print(max)
    print(name)