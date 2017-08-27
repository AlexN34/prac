#!/bin/python3

import sys

def super_reduced_string(s):
    sList = list(s)
    print(sList)
    prev = -1
    index = 0
    # Complete this function
    for char in sList[index:]:
        print("i: {} c: {}: prev: {}".format(index, char, prev))
        if index > 0:
            prev = sList[index-1]
        else:
            continue
        if char == prev:
            print("About to remove i: {} c: {}: prev: {}".format(index, char, prev))
            sList.remove(char)
            print(sList)
            sList.remove(prev)
            # print("delete")     #
            if len(sList) > 0:
                index = 0
            else:
                return "Empty String"
        index += 1

    return "".join(sList)

s = input().strip()
result = super_reduced_string(s)
print(result)
