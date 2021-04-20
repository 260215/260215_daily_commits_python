# Properties
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @property
    def pineapple_allowed(self):
        return False


pizza = Pizza(["cheese", "onion", "sausages", "black_olives", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
