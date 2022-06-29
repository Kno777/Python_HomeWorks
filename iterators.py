class Iterator:
    """Iterator class only for sequence(list, tuple)
    """
    def __init__(self, lst):
        """This is my constructor method, parametrs(self, sequence)
        Args:
            lst (_list_): sequence
        """
        self.lst = lst
        self.n = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            if self.n >= len(self.lst):
                raise StopIteration("\n\tSTOP: last element!")
            ls = self.lst[self.n]
            self.n += 1
            
            return ls
            

ls = [1,2,3,4]

it = Iterator(ls)

print(next(it))
print(next(it))
print(it.__next__())
