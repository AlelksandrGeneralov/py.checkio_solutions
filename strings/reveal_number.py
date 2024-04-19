
def reveal_num(line: str):
    
    res = sign = ""
    dot = False
    
    for char in line:
        if char == "-":
            sign = "-"
        elif char in "." and not dot:
            dot = True
            res += "."
        elif char.isdigit():
            res += char

    if dot:
        return float(sign + res)
    else:
        return int(sign + res)


print("Example:")
print(reveal_num("-aB%|_-+-2ADS.12+3.ADS1.2"))
