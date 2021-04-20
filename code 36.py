# Properties(Setter and Getter)
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self.pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter password : ")
            if password == "Suvam1999#":
                self.pineapple_allowed = value
            else:
                ValueError("Alert!")


pizza = Pizza(["cheese", "onion", "tomato", "black_olives"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)
