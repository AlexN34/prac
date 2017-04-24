#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

result = ""
for i in arr[::-1]:
    result += str(i) + " "

print (result.strip())
print ('Git test push from spacemacs second change')
