# -*- coding: utf-8 -*-
"""
DESCRIPTION:
In this kata you will be given an integer n, which is the number of times that is thown a coin. You will have to return an array of string for all the possibilities (heads[H] and tails[T]). Examples:

coin(1) should return {"H", "T"}
coin(2) should return {"HH", "HT", "TH", "TT"}
coin(3) should return {"HHH", "HHT", "HTH", "HTT", "THH", "THT", "TTH", "TTT"}

When finished sort them alphabetically.

In C and C++ just return a char* with all elements separated by, (without space):
coin(2) should return "HH,HT,TH,TT"

INPUT:
0 < n < 18

Careful with performance!! You'll have to pass 3 basic test (n = 1, n = 2, n = 3), many medium tests (3 < n <= 10) and many large tests (10 < n < 18)
"""

def coin(n):
    count = 1
    s = ['H','T']
    sides = ['H','T']
    sides1 = []
    
    if n > 18:
        n = 18
        
    while count < n:
        for i in s:
            for j in sides:
                sides1.append(i+j)
        sides = sides1
        sides1 = []
        count += 1
    return sides