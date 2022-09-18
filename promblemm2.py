
'''
This script is code stub for CodeChef problem code IFFOR1_PY
Filename:      IFFOR1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())

    # Write your code from here

while test_cases:
    n=int(input())
    
    for i in range(0,n):
        if i==0:
            print(i+3 ,end = ' ' )
        elif i%2==0:
            print(i*2 ,end = ' ' )
        else:
            print(i*i ,end = ' ' )
    print("")
    test_cases=test_cases -1
        