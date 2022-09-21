# cook your dish here

'''
This script is code stub for CodeChef problem code APLAM1_PY
Filename:      APLAM1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Import reduce module
from functools import reduce


# Function to generate the A.P. series
def generate_AP(a1, d, n):

    AP_series = []
    for i in range(0,n):
         AP_series.append(a1+i*d)
    # Complete this function to return A.P. series
    return AP_series


# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())

    # Write the code here to take the a1, d and n values

    while test_cases:
        
        # Once you have all 3 values, call the generate_AP function to find A.P. series and print it
        a1, d, n = input().split()
        a1=int(a1)
        d=int(d)
        n=int(n)
        AP_series = generate_AP(a1, d, n)
        b = ''.join(str(AP_series).split(','))
        # AP_series=AP_series.replace(',',' ')
        k=str(b)[1:-1]
        print(k)
        # Using lambda and map functions, find squares of terms in AP series and print it
        sqr_AP_series = list(map(lambda x : x*x, AP_series))
        c = ''.join(str(sqr_AP_series).split(','))
        u=str(c)[1:-1]
        print(u)

        # Using lambda and reduce functions, find sum of squares of terms in AP series and print it
        sum_sqr_AP_series = reduce(lambda x ,y : x+y,sqr_AP_series)
        print(sum_sqr_AP_series)

        test_cases=test_cases-1
