from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Ingresa el nombre del cafe que deseas ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink != "False":
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
            if is_enough_ingredients:
                is_payment_successful = money_machine.make_payment(drink.cost)
                if is_payment_successful:
                    coffee_maker.make_coffee(drink)
