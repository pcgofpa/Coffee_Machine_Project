# Imports
from coffee import coffee


def main_screen():
    operation_mode = input("press 1: to order, 2: Print report")
    if operation_mode == "1":
        user_order()
    elif operation_mode == "2":
        resource_report()
    elif operation_mode == "off":
        power_state()


def user_order():
    """Function to retrieve user order."""
    coffee_type = int(input("What would you like? 1. Espresso 2. Latte 3. Cappuccino): "))
    if coffee_type == 1:
        resource_report()
        make_coffee("espresso")
        print(f"Here is your espresso")
        resource_report()
    elif coffee_type == 2:
        resource_report()
        make_coffee("latte")
        print(f"Here is your latte")
        resource_report()
    elif coffee_type == 3:
        resource_report()
        make_coffee("cappuccino")
        print(f"Here is your cappuccino")
        resource_report()
    else:
        print("Invalid input")
# The prompt should show every time action has completed, e.g. once the drink is dispensed.
# The prompt should show again to serve the next customer.


def power_state():
    exit()
# Turn off the Coffee Machine by entering “off” to the prompt.
# For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code
# should end execution when this happens.


def resource_report():
    global Water_level, Milk_level, Coffee_level
    print(f"Current water level is: {Water_level}ml")
    print(f"Current milk level is: {Milk_level}ml")
    print(f"Current coffee level is: {Coffee_level}g")
    print(f"Machine currently has ${Current_Money} remaining")


def sufficient_resources():
    resource_report()
# Check resources sufficient?
# When the user chooses a drink, the program should check if there are enough resources to make that drink.
# E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the
# drink but print: “Sorry there is not enough water.”
# The same should happen if another resource is depleted, e.g. milk or coffee.

# def process_coins():
# Process coins.
# If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# Calculate the monetary value of the coins inserted.
# E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52


# def transaction_successful():
# Check transaction successful?
# Check that the user has inserted enough money to purchase the drink they selected. E.g Latte cost $2.50, but they
# only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money.
# Money refunded.”.
# But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and
# this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# If the user has inserted too much money, the machine should offer change.
# E.G. "Here is $2.45 dollars in change." The change should be rounded to 2 decimal places.

def make_coffee(order_type):
    global Water_level, Milk_level, Coffee_level, Current_Money
    for i in range(len(coffee)):
        if coffee["name"] == order_type:
            Water_level -= coffee["water"]
            Milk_level -= coffee["milk"]
            Coffee_level -= coffee["Coffee"]
            Current_Money += coffee["price"]
# Make Coffee
# If the transaction is successful and there are enough resources to make the drink the user selected, then the
# ingredients to make the drink should be deducted from the coffee machine resources.
#
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
#
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.


# Variables
Water_level = 60000
Milk_level = 20000
Coffee_level = 5000
Current_Money = float(50.00)
order_again = True

main_screen()
while order_again:
    if input(f"Would you like to place another order: 'y' or 'n'") == "n":
        order_again = False
    else:
        user_order()
