# -*- coding: utf-8 -*-
"""
DESCRIPTION:
Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

EXAMPLE:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
"""

def create_phone_number(n):
    #your code here
    
    def sum_num(lst):
        tot_num = ""
        lst = [str(i) for i in lst]
        for i in lst:
            tot_num += i
        return tot_num
    
    phone = [sum_num(n[0:3]),sum_num(n[3:6]),sum_num(n[6:10])]
    
    return "("+phone[0]+") "+phone[1]+"-"+phone[2]