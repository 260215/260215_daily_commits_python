# OOPS Concept(Inheritance)
class Animal:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs


class Dog(Animal):
    def bark(self):
        print("Bark")


class Cat(Animal):
    def meow(self):
        print("Meow")


class Tiger(Animal):
    def roar(self):
        print("Roar")


DOG = Dog("Brown", 4)
CAT = Cat("Yellow", 4)
TIGER = Tiger("White", 4)
print(DOG.color)
print(TIGER.legs)
CAT.meow()