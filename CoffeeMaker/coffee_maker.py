class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "agua": 300,
            "leche": 200,
            "cafe": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Agua: {self.resources['agua']}ml")
        print(f"Leche: {self.resources['leche']}ml")
        print(f"Cafe: {self.resources['cafe']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"No hay suficiente {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Aquie esta tu {order.name} ☕️. Que lo disfrute!")
