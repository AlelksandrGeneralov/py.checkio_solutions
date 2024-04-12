

def longest_substr(s: str) -> int:
    
    l = []
    ind = 0
    
    for char in s:
        my_str = ""
        counter = 0
        
        for char in s:
            if char not in my_str:
                my_str += char
                counter += 1
            else:
                break
        
        l.append(counter)
        print(s)
        s = s[1:]
        ind += 1
    return max(l)
    
print("Example:")
print(longest_substr("dvdf"))