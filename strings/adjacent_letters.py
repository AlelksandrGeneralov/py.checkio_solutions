
def adjacent_letters(line: str) -> str:
    
    if line == "":
        return ""
    
    l = list(line)
    
    def del_func(l):
        i = 0
        while i < len(l) - 1:
            if l[i] == l[i + 1]:
                l.pop(i)
                l.pop(i)
                del_func(l)
            i += 1
        return "".join(l)   

    return del_func(l)


print("Example:")
print(adjacent_letters("abbaca"))