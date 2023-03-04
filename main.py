from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu=Menu()
coffee_maker = CoffeeMaker()
money_machine =MoneyMachine()


machine_status = True

while machine_status:
    option = menu.get_items()
    user_prompt=input(f"what wouls you like to have ?{option}")
    if user_prompt == "off":
        machine_status = False
    elif user_prompt ==   "report":
        coffee_maker.report()
        money_machine.report()

    else:

        drink = menu.find_drink(user_prompt)
        if coffee_maker.is_resource_sufficient(drink) and if  money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





