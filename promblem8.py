
'''
This script is code stub for CodeChef problem code D2BIN1_PY
Filename:      D2BIN1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

# Function to calculate Euclidean distance between two points
def dec_to_binary(n):

    bin_num = []
    if n > 1:
        bin_num = dec_to_binary( n//2)
        k=n % 2
    else:
        k=n % 2
    bin_num.append(k)
    return bin_num
    # print(n % 2, end = '')


    # Complete this function to return binary equivalent output of the given number 'n' in 8-bit format

    # return bin_num
# bin_num =[]

# Main function
if __name__ == '__main__':
    
    # take the T (test_cases) input
    test_cases = int(input())
    # bin_num =[]

    # Write the code here to take the n value
    for case in range(1,test_cases+1):
        # take the n input values
        n = int(input())

        # print (n)
        
        # dec_to_binary(n)
        # print("\n")
        # Once you have the n value, call the dec_to_binary function to find the binary equivalent of 'n' in 8-bit format
        bin_num = dec_to_binary(n)
        k=8-len(bin_num)
        for i in range(0,k):
            print("0",end = '')
        for i in range(0,len(bin_num)):
            # r=r+p[i]
            print(bin_num[i],end = '')
        print("\n")
