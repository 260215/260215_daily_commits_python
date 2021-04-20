# Static methods
class Pizza(object):
    @classmethod
    def validate_topping(cls, i):
        pass


class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No Pineapples!")
        else:
            return True

    ingredients = ["cheese", "onions", "chicken", "black_olives", "jalapanos"]
    if all(Pizza.validate_topping(i) for i in ingredients):
        pizza = Pizza(ingredients)
