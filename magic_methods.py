class Square:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # __repr__ is the literal constructor code printed:
        return f"Square({self.x}, {self.y})"
    
    def __str__(self):
        # __str__ is the normal human readable version:
        return f"{self.x}, {self.y}"

    def __add__(self, other):
        # add two squares together to create a new one
        return Square((self.x + other.x), (self.y + other.y))
    
    def __eq__(self, other):
        # check if the squares are equal:
        return self.x == other.x and self.y == other.y

    def __len__(self):
        # len()
        return int(self.x * self.y)

if __name__ == "__main__":
    sq1 = Square(2, 2)
    sq2 = Square(4, 4)
    print(repr(sq1))
    print(sq1)
    print(repr(sq2))
    print(sq2)
    
    print(f"sq1 == sq2: {sq1 == sq2}")

    sq3 = sq1 + sq2
    print(repr(sq3))
    print(sq3)
    print(len(sq3))

    
    