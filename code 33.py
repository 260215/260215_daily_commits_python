# Class Methods
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    @classmethod
    def new_square(cls, side):
        return cls(side, side)


square = Rectangle.new_square(5)
print(square.calculate_area())
