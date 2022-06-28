def my_join(data, sep):
    """Concatenate any number of strings
    
    Args:
        data (sequnce): 
        sep (_type_): 
        
    Returns:
        _str_: 
    """
    
    ls = []
    for val in data:
            ls.append(val)
            ls.append(sep)
    
    if ls[0] == type(str):
            s = ""
            try:
                    for ch in ls:
                            s = s + ch
                            
            except TypeError as e:
                    print(f"{e}\n\n your data wrong!")
                    exit(0)
    else:
            s = ""
            try:
                  arr = [str(i) for i in ls]
                  for ch in arr:
                          s = s + ch   
                            
            except TypeError as e:
                    print(f"{e}\n\n your data wrong!")
                    exit(0)
    return s
        
ls = [1, 2, 3]
print(my_join(ls, ""))