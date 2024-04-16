
def flatten(dictionary, parent_key: str = '', sep: str ='/'):
    
    from collections.abc import MutableMapping
   
    items = []
    
    for k, v in dictionary.items():
        new_key = parent_key + sep + k if parent_key else k

        if v == {}:
            items.append((new_key, "")) #use append method because we add new tuple to list
        elif isinstance(v, MutableMapping): #check if v is dictionary...
            items.extend(flatten(v, new_key, sep).items()) #use extend method because we add new list of tuples to list
        else:
            items.append((new_key, v))
    return dict(items) #unpack list of tuples into dict

print("Example:")
print(flatten({
        "name": {"first": "One", "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {"place": {"zone": "1", "cell": "2"}},
    }))