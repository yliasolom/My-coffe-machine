#again what we have:
water = 400
milk = 540
beans = 120
cups = 9
money = 550


#add class to prevent running the function
class ResourceError(Exception):
    pass

def output_status():
    print("The coffee machine has:")
    print(water, "ml of water")
    print(milk, "ml of milk")
    print(beans, "g of coffee beans")
    print(cups, "of disposable cups")
    print(f'${money} of money')


def chose_action():
    choice = input("Write action (buy, fill, take, remaining, exit):")
    return choice


def chose_drink():
    response = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:"))
    if response=='back':
        return 0
    return int(response)


# add enough function:
def enough(water_need=0, milk_need=0, beans_need=0):
    if water<water_need:
        print('Sorry, not enough water!\n')
        raise ResourceError
    elif milk<milk_need:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    elif beans<beans_need:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    elif cups < 1:
        print('Sorry, not enough cups\n')
        raise ResourceError
    print('I have enough resources, making you a coffee!\n')


def buy():
    global water, milk, beans, cups, money
    cups -= 1
    drink = chose_drink()

    try:
        if drink==0:
            pass
        elif drink == 1:  # espresso
            enough(water_need=250, beans_need=16)
            money += 4
            water -= 250
            beans -= 16
        elif drink == 2:  # latte
            enough(water_need=350, milk_need=75, beans_need=20)
            money += 7
            water -= 350
            milk -= 75
            beans -= 20
        elif drink == 3:  # cappuccino
            enough(water_need=200, milk_need=100, beans_need=12)
            money += 6
            water -= 200
            milk -= 100
            beans -= 12
        else:
            raise ValueError(f'Unknown drink {drink}')
    except ResourceError:
        pass


def fill():
    global water, milk, beans, cups
    water += int(input("Write how many ml of water you want to add:"))
    milk += int(input("Write how many ml of milk you want to add:"))
    beans += int(input("Write how many grams of coffee beans you want to add:"))
    cups += int(input("Write how many disposable cups you want to add:"))


def take():
    global money
    print("I gave you $", money)
    money = 0


# lets create correct format with 'main'
def main():
    while True:
        action = chose_action()
        if action == "buy":
            buy()
        elif action == "fill":
            fill()
        elif action == "take":
            take()
        elif action == 'exit':
            break
        elif action =='remaining':
            output_status()
        else:
            raise ValueError(f'Unknown command {action}')


if __name__ == '__main__':
    main()

