
def reveal_num(line: str):
    
    res = sign = ""
    dot = False
    
    for char in line:
        if char in "+-" and not res:
            sign = "-"*(char == "-")
        elif char in "." and not dot:
            dot = True
            res += "."
        elif char.isdigit():
            res += char
        
    if res:
        return(int, float)[dot](sign + res)


print("Example:")
print(reveal_num("-aB%|_-+-2ADS.12+3.ADS1.2"))