#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    sum_diagonal_one = 0
    sum_diagonal_two = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == j:
                sum_diagonal_one += arr[i][j]
            if i + j == len(arr) - 1:
                sum_diagonal_two += arr[i][j]
    return abs(sum_diagonal_one - sum_diagonal_two)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    # print(result)
    fptr.write(str(result) + '\n')
    fptr.close()

'''
3
11 2 4
4 5 6
10 8 -12
'''