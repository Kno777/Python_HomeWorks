"""This is my Double type:
Returns:
    Floating Double Number:
"""

class Double:
    def __init__(self, value=0.0, /):
        """My Constructor give one argument float type

        Args:
            value (float, optional): _description_. Defaults to 0.0.
        """
        self._value = float(value)
    
    # Operator	Magic Method
    
    def __add__(self, other):
        """Adding two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value + other._value
        """
        return self._value + other._value
    
    def __radd__(self, other):
        """Adding two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: other._value + value._value
        """
        return other._value + self._value
    
    def __iadd__(self, other):
        """Adding two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value += other._value
        """
        self._value += other._value
        return self._value

    def __sub__(self, other):
        """Sub two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value - other._value
        """
        return self._value - other._value
    
    def __isub__(self, other):
        """Sub two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value -= other._value
        """
        self._value -= other._value
        return self._value
    
    def __mul__(self, other):
        """Mul two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value * other._value
        """
        return self._value * other._value
    
    def __imul__(self, other):
        """Mul two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value *= other._value
        """
        self._value *= other._value
        return self._value
    
    def __truediv__(self, other): # /
        """Div two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value / other._value
        """
        return self._value / other._value
    
    def __floordiv__(self, other): # //
        """Div two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value // other._value
        """
        return self._value // other._value
    
    def __mod__(self, other):
        """Moduls two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value % other._value
        """
        return self._value % other._value
    
    def __pow__(self, other):
        """Pow two Double variable

        Args:
            other (double): 

        Returns:
            _Double_: self._value ** other._value
        """
        return self._value ** other._value
    
    def __str__(self):
        return f"Double: {self._value}"
    
    def __abs__(self):
        """Return the absolute value of the argument.

        Returns:
            _type_: self._value
        """
        if self._value <= 0:
            return abs(self._value)
        return self._value
    
    
    # Logic 
    def __and__(self, other):
        return self._value & other._value
    
    def __or__(self, other):
        return self._value | other._value
    
    def __xor__(self, other):
        return self._value ^ other._value
    
    def __lshift__(self, other): # <<
        return self._value << other._value
    
    def __rshift__(self, other): # >>
        return self._value >> other._value
    
    
    # Comparison Operators :
    
    def __gt__(self, other): # >
        return self._value > other._value
    
    def __lt__(self, other): # < 
        return self._value < other._value
    
    def __le__(self, other): # <=
        return self._value <= other._value
    
    def __ge__(self, other): # >=
        return self._value >= other._value
    
    def __eq__(self, other): # ==
        return self._value == other._value
    
    def __ne__(self, other): # !=
        return self._value != other._value
    
    
d = Double(4)
c = Double(2)

k = Double(-10) 

print(k.__abs__())
