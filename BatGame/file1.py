import random
from os import system, name


def main():
    print("Welcome to Cameron's Game of Chance\n\n")
    menu()


def menu():
    print("1. Start")
    print("2. Instructions")
    print("3. Exit")

    menu_input = input("Select a menu option")

    if menu_input == "1":
        start_1()
    elif menu_input == "2":
        instructions()
    elif menu_input == "3":
        end()
    else:
        print("You have entered an incorrect command. Please try again.\n")
        return menu()


def start_1():
    clear()
    print("You have run into bad guys. Their forces are...\n")
    return troops_1()


def instructions():
    print("Please follow the onscreen instructions for each step of the game.\n")
    return menu()


def end():
    print("!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    print("!~! Thanks for Playing! !~!")
    print("!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    return exit(0)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def troops_1():
    t1 = random.randint(0, 4)
    if t1 == 1:
        print("You have encountered a few farmers armed with pitchforks.\n")
    elif t1 == 2:
        print("You have encountered a lot of farmers armed with pitchforks and torches.\n")
    elif t1 == 3:
        print("You have encountered an entire village of farmers armed with pitchforks, torches, and slingshots.\n")
    elif t1 == 4:
        print("You have encountered multiple villages of farmers armed with pitchforks, "
              "torches, slingshots, and bow'n'arrows.\n")


if __name__ == '__main__':
    main()
