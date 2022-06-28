def split(string, delimiter):
    """Return a list of the words in the string, using sep as the delimiter string.
    
    Args:
        string (_type_): 
        delimiter (_type_):
        
    Raises:
        ValueError: Empty Separator
        
    Returns:
        _List_: 
    """
    result_list = []
    if not delimiter:
        raise ValueError("Empty Separator")

    if not string:
        return [string]

    start = 0
    for index, char in enumerate(string):
        if char == delimiter:
            result_list.append(string[start:index])
            start = index + 1
            
    if start == 0:
        return [string]

    result_list.append(string[start:index + 1])
    
    return result_list

s = "hello.World.Kno"
print(split(s, '.'))