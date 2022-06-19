def my_sum(a:int, b:int, c:int):
    """This function adds 3 arguments.
    
    Args:
        a (_int):
        b (_int): 
        c (_int):

    Returns:
        int(a + b + c): 
    """
    return a + b + c


def my_map(func, lst, *iterable):
    """This function gets first parameter function
       and the second parameter sequence.(List, Tuple, Set, ...).
       Returns Generator Object.
    Args:
        func (_func): 
        lst (sequence): 

    Yields:
        Return : yield
    """
    for args in zip(lst, *iterable):
        yield func(*args)
    
    
ls1 = [1, 2, 3]
ls2 = [10, 20, 30]
ls3 = [100, 200, 300]

mp = my_map(my_sum, ls1, ls2, ls3)
print(list(mp))



base = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
exp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

pw = list(my_map(pow, base, exp))
print(pw)