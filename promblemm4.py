
'''
This script is code stub for CodeChef problem code DIST1_PY
Filename:      DIST1_PY_solution.py
Created:       27/09/2021
Last Modified: 27/09/2021
Author:        e-Yantra Team
'''

 
# Import any required module/s

from dis import dis
import math

# Function to calculate Euclidean distance between two points
def compute_distance(x1, y1, x2, y2):

    distance = 0
    
    distance=((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    distance=math.sqrt(distance)
    return distance
    # Complete this function to return Euclidean distance and
    # print the distance value with precision up to 2 decimal places


# Main function
if __name__ == '__main__':
    
    # Take the T (test_cases) input
    test_cases = int(input())
    
    while test_cases:
        x1 ,y1 ,x2 ,y2 =input().split()
        # h=input()
        # k=h.split()
        x1=int(x1)
        y1=int(y1)
        y2=int(y2)
        x2=int(x2)


    # Write the code here to take the x1, y1, x2 and y2 values
    
    
        # Once you have all 4 values, call the compute_distance function to find Euclidean distance
        distance = compute_distance(x1, y1, x2, y2)
        # print(distance)
        d_f="{:.2f}".format(distance)
        print(d_f)
        test_cases = test_cases - 1