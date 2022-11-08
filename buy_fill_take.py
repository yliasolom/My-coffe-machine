# # Buy, fill, take!
# #what we have:

water = 400
milk = 540
coffee = 120
disposable_cups = 9
money = 550


def output_status():
    print("The coffee machine has:")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(coffee, "g of coffee beans")
    print(disposable_cups, "of disposable cups")
    print(f'${money} of money')


def chose_action():
    choice = input("Write action (buy, fill, take):")
    return choice

def chose_drink():
    choice = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: "))
    return choice

def fill():
    global water, milk, coffee, disposable_cups
    water += int(input("Write how many ml of water you want to add:"))
    milk += int(input("Write how many ml of milk you want to add:"))
    coffee += int(input("Write how many grams of coffee beans you want to add:"))
    disposable_cups += int(input("Write how many disposable cups you want to add:"))


def take():
    global money
    print("I gave you $", money)
    money = 0

def buy():
    global water, milk, coffee, disposable_cups, money
    disposable_cups -= 1
    drink = chose_drink()
    if drink == 1:  # espresso
        water -= 250
        coffee -= 16
        money += 4
    elif drink == 2:  # latte
        water -= 350
        milk -= 75
        coffee -= 20
        money += 7
    elif drink == 3:  # cappuccino
        water -= 200
        milk -= 100
        coffee -= 12
        money += 6
    else:
        raise ValueError(f'Unknown drink {drink}')

output_status()
action = chose_action()
if action == "buy":
    buy()
elif action == "fill":
    fill()
elif action == "take":
    take()
else:
    raise ValueError(f'Unknown action {action}')
output_status()
