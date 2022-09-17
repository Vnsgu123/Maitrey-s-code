
def ispalindrone(s):
    return s==s[::-1]
    

t=input()
t=int(t)

while t:
    a=input()
    c=a.upper()

    b=ispalindrone(c)
    if b:
        print("it is apalindrome")
    else:
        print("it is not a palindrome")
    t=t-1  
  
