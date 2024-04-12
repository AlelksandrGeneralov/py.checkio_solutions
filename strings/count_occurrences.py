

def count_occurrences(main_str: str, sub_str: str) -> int:
    
    ind = 0
    counter = 0
    main_str = main_str.lower()
    sub_str = sub_str.lower()
 
    """Search starts from 0 index in main_str and loops till first occurence or till the end element (index -1).
    Then search starts from next index after first occurence.
    """ 
    
    while main_str.find(sub_str, ind) != -1:
        print(main_str.find(sub_str, ind))
        ind = main_str.find(sub_str, ind) + 1 # Increment index for next loop of search.
        counter += 1
        
    return counter
    


print(count_occurrences("ssappleappleapple", "appleapple"))

