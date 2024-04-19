
def reveal_num(line: str):
    
    res = sign = ""
    dot = False
    
    for char in line:
        if char in "+-" and not res:
            sign = "-"*(char == "-")
"""boolean b = (char == "-") will evaluate to b = 0 (False) or b = 1 (True)
in this context so that "-"*b will be either "" 
(in this case no need to redefine since sign is already the empty string) or "-""""            
        elif char in "." and not dot:
            dot = True
            res += "."
        elif char.isdigit():
            res += char
"""Explanation: (int, float) creates a tuple. 
boolean dot will again evaluate as an integer in this context to grab the 0th (False) or 1st (True) element of that tuple, 
which is a string to number conversion function in either case, to finally apply it to sign + res"""        
    if res:
        return(int, float)[dot](sign + res)


print("Example:")
print(reveal_num("-aB%|_-+-2ADS.12+3.ADS1.2"))
