def my_replace(text:str, old:str, new:str):
    """This is my replace function, this change old line to new line

    Args:
        text (str): 
        old (str): 
        new (str): 

    Returns:
        _str_: ls
    """
    ls = []
    if old not in text:
            return f"{old} not found in text"
    
    for char in text:
            if char in old:
                    ls.append(new)
            else:
                    ls.append(char)
            
    if ls.count(new) > 2:
            ls.remove(new)
            
    ls = ''.join(ls)    
    
    return ls

s = "Python Better"

print(my_replace(s, "B", "Kn"))