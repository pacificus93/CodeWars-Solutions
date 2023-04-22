# -*- coding: utf-8 -*-
"""
DESCRIPTION:
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)
where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
"""

def longest_repetition (s):
    lst = []
    s = "_" + s
    
    if len(s) == 1:
        return ('',0)
    
    # Gather length for each consecutive repetition
    
    for i in range(1,len(s)):
        if s[i] != s[i - 1]:
            lst.append([s[i],1])
            continue
        lst[len(lst) - 1][1] += 1
    
    m = max([j[1] for j in lst])
    
    return tuple([i for i in lst if i[1] == m][0])