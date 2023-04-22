# -*- coding: utf-8 -*-
"""
DESCRIPTION:
You are the "computer expert" of a local Athletic Association (C.A.A.). 
Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. 

For example here is a string showing the individual results of a team of 5 runners:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"


Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) 
with one or two digits. Substrings in the input string are separated by ,  or ,.


To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range : difference between the lowest and highest values. 

Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. 


Your task is to return a string giving these 3 values. 

For the example given above, the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:
if a result in seconds is ab.xy... it will be given truncated as ab.
if the given string is "" you will return ""
"""

import numpy as np
import math as m
def stat(strg):
     # your code
    
    class CAA_Statistics:
        def __init__(self,results_info):
            self.results_info = results_info
        def string_to_list(self,lst = []):
            #Turning string input into the list of team results
            
            for i in [el.split(',') for el in str(self.results_info).split(', ')]:
                lst += i
            return lst
        def element_to_sec(self,elem,time_result = 0,sec =  60):
            #Turning element of the form HH|MM|SS into seconds (type : integer)
            
            elem = elem.split('|')
            for i in range(len(elem)):
                time_result+=int(elem[i])*sec**(2 - i)    
            return time_result
        def stats(self,lst=[]):
            #Getting necessary statistics (according to initial task)
            
            lst = self.string_to_list()
            lst = [self.element_to_sec(i) for i in lst]
            info = [m.trunc(max(lst)-min(lst)),m.trunc(np.average(lst)),m.trunc(np.median(lst))]
            return info
        def sec_to_elem(self,sec=60,elem = ""):
            
            def number_output(numb):
                return "0" + str(numb) if numb < 10 else str(numb)
            
            for i in range(2):
                elem = "|"+number_output(int(sec % 60)) + elem
                sec -= sec % 60
                sec /= 60
            elem = number_output(int(sec)) + elem
            return elem
        def message(self,data = [],txt = ["Range: "," Average: "," Median: "]):
            fin_txt = ""
            data = self.stats()
            txt = [txt[i]+self.sec_to_elem(data[i]) for i in range(len(txt))]
            for i in range(3):
                fin_txt+=txt[i]
            return fin_txt
    
    return CAA_Statistics(strg).message()