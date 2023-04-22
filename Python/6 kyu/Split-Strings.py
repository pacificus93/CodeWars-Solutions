# -*- coding: utf-8 -*-
"""
DESCRIPTION:
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    length = len(list(s))
    
    splitter = lambda s : [list(s)[2 * i] + list(s)[2 * i + 1] for i in range(int((len(s) - 2) / 2) + 1)]
    
    if length % 2 == 0:
        return splitter(s)
    s += "_"
    return splitter(s)