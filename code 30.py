# OOP Concepts (Class and Object)
class bike:
    def __init__(self, model, color, stroke, cc):
        self.model = model
        self.color = color
        self.stroke = stroke
        self.cc = cc

    def exhaust(self):
        print("The Loud ones!!")


BIKE = bike("MV Augusta", "Red", 6, 1500)
print(BIKE.model)
print(BIKE.color)
print(BIKE.stroke)
print(BIKE.cc)
BIKE.exhaust()

