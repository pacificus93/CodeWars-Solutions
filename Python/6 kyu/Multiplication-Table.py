# -*- coding: utf-8 -*-
"""
DESCRIPTION:
Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]
"""

def multiplication_table(size):
    return [[(j+1)*(i+1) for j in range(size)] for i in range(size)]