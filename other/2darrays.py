#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

# print (arr)
maxSum = -sys.maxsize # maximum long in python
for i in range(len(arr) - 2):
    for j in range (len(arr[i]) - 2):
        # print ("cur indices: i:%d j: %d" % (i, j))
        # print (arr[i])
        #with slices, i:j j non inclusive
        s = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
        # Ugly - many for loops. Can use sums of slices instead
        # for hRow in range(3):
        #     for hCol in range(3):
        #         if hRow == i+1 and (hCol == j or hCol == j + 2):
        #             continue
        #         else:
        #             # print ("cur hterm: row:%d col: %d" % (hRow, hCol))
                    # hsum += arr[i + hRow][j + hCol] 
        # print (s)
        maxSum = max(s, maxSum)

print (maxSum)
