#!/usr/bin/python
# Given an array, find the nearest smaller element G[i]
# for every element A[i] in the array such that the element
# has an index smaller than i.
"""
G[i] for an element A[i] = an element A[j] such that
  j is maximum possible AND
  j < i AND
  A[j] < A[i]
"""
import pytest
def NearestSmallerElement(A):
    result = []
    hit = False
    for index, elt in enumerate(A):
        if index > 0:
            print(index)
            j = index
            print(j)
            while True:
                j -= 1
                if A[j] < A[index]:
                    result.append(A[j])
                    hit = True
                    break
                print(j)
                if j <= 0:
                    print(result)
                    if not hit:
                        result.append(-1)
                        hit = False
                    break
        else:
            result.append(-1)
    return result

class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        A = [list(row) for row in A]
        # Sounds like flood fill..
        def fill(row, col):
            if row < 0 or row >= len(A) or col < 0 or col >= len(A[row]) or A[row][col] != 'X':
                return
            A[row][col] = '-'
            fill(row-1, col)
            fill(row+1, col)
            fill(row, col-1)
            fill(row, col+1)
        count = 0
        for row in range(len(A)):
            for col in range(len(A[row])):
                char = A[row][col]
                if char == 'X':
                    count += 1
                    fill(row, col)
        return count

