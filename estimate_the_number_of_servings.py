def count_supply(water, milk, beans, cups):
    possible = min([water // 200, milk // 50, beans // 15])
    # print(possible) - check status

    if possible == cups:
        message = 'Yes, I can make that amount of coffee'
    elif possible > cups:
        message = f'Yes, I can make that amount of coffee (and even {possible - cups} more than that)'
    else:
        message = f'No, I can make only {possible} cups of coffee'
    return message

def main():
    water = int(input('Write how many ml of water the coffee machine has: '))
    milk = int(input('Write how many ml of milk the coffee machine has: '))
    beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
    cups = int(input('Write how many cups of coffee you will need: '))
    print(count_supply(water, milk, beans, cups))


if __name__ == '__main__':
    main()