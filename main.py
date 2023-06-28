# Imports
from coffee import coffee


def user_order():
    """Function to retrieve user order."""
    global coffee_choice
    coffee_type = input("What would you like? 1. Espresso 2. Latte 3. Cappuccino): ")
    if coffee_type == "1":
        coffee_choice = coffee[0]
        process_coins()
        transaction_successful()
        return coffee_choice
    elif coffee_type == "2":
        coffee_choice = coffee[1]
        process_coins()
        transaction_successful()
        return coffee_choice
    elif coffee_type == "3":
        coffee_choice = coffee[2]
        process_coins()
        transaction_successful()
        return
    elif coffee_type == "off":
        power_state()
    elif coffee_type == "report":
        resource_report()
    else:
        print("Invalid input")


# Turn off the Coffee Machine by entering “off” to the prompt.
def power_state():
    """Function to turn off the machine."""
    exit()


def resource_report():
    """Function to print a report of the current resource level. """
    global Water_level, Milk_level, Coffee_level
    print(f"Current water level is: {Water_level}ml")
    print(f"Current milk level is: {Milk_level}ml")
    print(f"Current coffee level is: {Coffee_level}g")
    print(f"Machine currently has ${Current_Money} remaining")


def sufficient_resources():
    """Function to determine if there is enough resources in the machine to make the user's coffee."""
    global Water_level, Milk_level, Coffee_level
    coffee_name = coffee_choice["name"]
    req_water = coffee_choice["water"]
    req_milk = coffee_choice["milk"]
    req_coffee = coffee_choice["Coffee"]
    if req_water <= Water_level and req_milk <= Milk_level and req_coffee <= Coffee_level:
        make_coffee()
    elif req_water > Water_level:
        print(f"Insufficient water for your {coffee_name}:")
    elif req_coffee > Coffee_level:
        print(f"Insufficient coffee for your {coffee_name}:")
    elif req_milk > Milk_level:
        print(f"Insufficient milk for your {coffee_name}:")


def process_coins():
    """Function to take user coin payment and calculate total payment received."""
    global total_payment
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25
    pay_quarter = int(input("How many quarters?"))
    pay_dime = int(input("How many dimes?"))
    pay_nickel = int(input("How many nickels?"))
    pay_penny = int(input("How many pennies?"))
    quarter_payment = quarter * pay_quarter
    dime_payment = dime * pay_dime
    nickel_payment = nickel * pay_nickel
    penny_payment = penny * pay_penny
    total_payment = round(quarter_payment + dime_payment + nickel_payment + penny_payment, 2)
    return total_payment


def transaction_successful():
    """Function to determine if user inserted enough change for their coffee choice."""
    global Current_Money
    coffee_name = coffee_choice["name"]
    coffee_price = coffee_choice["price"]
    if total_payment >= coffee_price:
        correct_change = round(total_payment - coffee_price, 2)
        Current_Money += total_payment
        sufficient_resources()
        print(f"Your {coffee_name} cost ${coffee_price}, you paid ${total_payment}. Your change is ${correct_change}")
        return Current_Money
    elif total_payment < coffee_price:
        in_correct = round(coffee_price - total_payment, 2)
        print(f"Your {coffee_name} cost ${coffee_price}, you paid ${total_payment}. You are ${in_correct} short.")


def make_coffee():
    """Function to make the coffee."""
    global Water_level, Milk_level, Coffee_level, coffee_choice
    coffee_name = coffee_choice["name"]
    req_water = coffee_choice["water"]
    req_milk = coffee_choice["milk"]
    req_coffee = coffee_choice["Coffee"]
    Water_level -= req_water
    Milk_level -= req_milk
    Coffee_level -= req_coffee
    print(f"Here is your {coffee_name}. Enjoy!")


# Variables
Water_level = 300
Milk_level = 200
Coffee_level = 100
Current_Money = float(25.00)
order_again = True
total_payment = 0
coffee_choice = coffee[0]


while order_again:
    user_order()
    if input(f"Would you like to place another order: 'y' or 'n' ") == "n":
        order_again = False
    else:
        user_order()
