# -*- coding: utf-8 -*-
"""
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) // returns FFFFFF
rgb(255, 255, 300) // returns FFFFFF
rgb(0,0,0) // returns 000000
rgb(148, 0, 211) // returns 9400D3
"""

def rgb(r, g, b):
    def converter(val):
        output = ""
        hex_ = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G']
        
        def check_boundary(val):
            """
            Rounding value that fall out of the range described to the closest valid value.
            """
            if val > 255:
                return 255
            if val < 0:
                return 0
            return val
        
        val = check_boundary(val)
        
        while val > 16:
            output += hex_[int((val - val % 16) / 16)]
            val = val % 16
        
        output += hex_[val]
        
        if len(output) == 1:
            output = "0" + output
        
        return output
    
    return converter(r) + converter(g) + converter(b)