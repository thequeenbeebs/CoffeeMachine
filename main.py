
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resources(coffee_order, cur_resources):
    order = MENU[coffee_order]
    for ingredient in order['ingredients']:
        if order['ingredients'][ingredient] > cur_resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def transaction_successful(current_money, drink_order):
    drink_cost = MENU[drink_order]['cost']
    if drink_cost > current_money:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif current_money > drink_cost:
        change = current_money - drink_cost
        print(f"Here is ${change:.2f} dollars in change.")
        return True
    else:
        return True


def deduct_resources(cur_resources, drink_order):
    order = MENU[drink_order]['ingredients']
    for ing in order:
        cur_resources[ing] -= order[ing]
    return cur_resources


def make_coffee():
    current_resources = resources
    machine_money = 0
    user_money = 0
    turning_off = False
    while not turning_off:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "off":
            turning_off = True
        elif order == "report":
            print(f"Water: {current_resources['water']} ml")
            print(f"Milk: {current_resources['milk']} ml")
            print(f"Coffee: {current_resources['coffee']} g")
            print(f"Money: ${machine_money}")
        else:
            if enough_resources(order, current_resources):
                print("Please insert coins.")
                quarters = int(input("How many quarters?: ")) * .25
                dimes = int(input("How many dimes?: ")) * .1
                nickels = int(input("How many nickels?: ")) * .05
                pennies = int(input("How many pennies?: ")) * .01
                user_money += quarters + dimes + nickels + pennies
                if transaction_successful(user_money, order):
                    machine_money += user_money
                    current_resources = deduct_resources(current_resources, order)
                    print(f"Here is your {order} ☕. Enjoy!")
                else:
                    user_money = 0


make_coffee()



