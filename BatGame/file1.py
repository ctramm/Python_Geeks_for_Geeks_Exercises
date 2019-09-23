import random
import os


def main():
    print("Welcome to Cameron's Game of Chance\n\n")
    pause()
    menu()


def menu():
    clear()
    print("1. Start")
    print("2. Instructions")
    print("3. Exit")

    menu_input = input("Select a menu option\n")

    if menu_input == "1":
        start_1()
    elif menu_input == "2":
        instructions()
    elif menu_input == "3":
        end()
    else:
        clear()
        print("You have entered an incorrect command. Please try again.\n")
        pause()
        return menu()


def instructions():
    clear()
    print("Please follow the onscreen instructions for each step of the game.\n")
    pause()
    return menu()


def run():
    clear()
    print("You ran away safely!")
    pause()
    return menu()


def lose_fight():
    clear()
    print("Sorry, you have lost the battle. Better luck next time.")
    pause()
    return menu()


def end():
    clear()
    print("!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    print("!~! Thanks for Playing! !~!")
    print("!~!~!~!~!~!~!~!~!~!~!~!~!~!")
    pause()
    return exit(0)


def clear():
    os.system('cls')


def pause():
    os.system('pause')


# Level 1
def start_1():
    clear()
    print("You have run into bad guys. Their forces are...\n")
    pause()
    return troops_1()


def troops_1():
    clear()
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
    else:
        print("You spontaneously combusted.")
        pause()
        return end()
    print("You have a high chance of winning.")
    a1 = input("would you like to fight or run? (fight/run)\n")
    if a1.lower() == "fight" or a1.lower() == "f":
        return fight_1()
    else:
        return run()


def fight_1():
    clear()
    print("You have chosen to fight.")
    print("The battle is waging...")
    pause()
    f1 = random.randint(0, 4)
    if f1 == 1:
        return lose_fight()
    else:
        return win_fight_1()


def win_fight_1():
    clear()
    print("Congrats, you won the fight!")
    w1 = input("Would you like to save?")
    if w1.lower() == "yes" or w1.lower() == "y":
        return save_1()
    else:
        return start_2()


def save_1():
    clear()
    print("Your game has been saved.")
    s1 = input("Do you wish to continue or quit?")
    if s1.lower() == "continue" or s1.lower() == "c":
        return start_2()
    else:
        return menu()


# Level 2
def start_2():
    clear()
    print("Congratulations!~! You have reached level 2.")
    pause()
    clear()
    print("You have run into more bad guys. Their forces are...")
    t2 = random.randint(0, 4)
    if t2 == 1:
        print("A horde of guards\n")
    elif t2 == 2:
        print("A few guards\n")
    elif t2 == 3:
        print("An entire army of guards\n")
    elif t2 == 4:
        print("A lot of guards\n")
    else:
        print("You spontaneously combusted.")
        pause()
        return end()
    print("You have a moderate chance of winning.")
    a2 = input("Would you like to fight or run? (fight/run)")
    if a2 == "fight" or a2 == "f":
        return fight_2()
    else:
        return run()


def fight_2():
    clear()
    print("You have chosen to fight.")
    print("The battle is waging...")
    pause()
    f1 = random.randint(0, 4)
    if f1 == 1:
        return lose_fight()
    else:
        return win_fight_2()


def win_fight_2():
    clear()
    print("Your game has been saved.")
    s1 = input("Do you wish to continue or quit?")
    if s1.lower() == "continue" or s1.lower() == "c":
        return save_2()
    else:
        return menu()


def save_2():
    clear()
    print("Your game has been saved.")
    s1 = input("Do you wish to continue or quit?")
    if s1.lower() == "continue" or s1.lower() == "c":
        return start_3()
    else:
        return menu()


# Level 3
def start_3():
    clear()
    print("Congratulations!~!~ You have reached level 3.")
    print("Unfortunately, level 3 is still being created...")
    print("Please come back soon!")
    pause()
    return end()


if __name__ == '__main__':
    main()
