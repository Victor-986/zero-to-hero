class Value():
    def __init__(self, num):
        self.num = num 

    def __mul__(self, other):
        return self.num * other.num

    def __add__(self, other):
        return self.num + other.num

    def __radd__(self, other):
        if isinstance(other, int):
            return self.num + other
        return NotImplemented
        
    def __repr__(self):
        return f"Value({self.num})"

total = Value(2) * Value(3) + Value(1)
print(total)