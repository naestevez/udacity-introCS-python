import random

print("Roll the dice")
ready = input("Are you ready to roll the dice? (Y/N) ")

def roll_dice():
    dice = [1, 2, 3, 4, 5, 6]
    print(random.choice(dice))

def confirm_play(ready):
    if ready == "Y" or ready == 'y':
        roll_dice()
        print("Would you like to roll again?")
    elif ready == "N" or ready == 'n':
        dble_check = input("Are you sure? (Y/N) ")
        if dble_check == "Y" or dble_check == "y":
            print("Ok please exit")
        elif ready == "N" or ready == 'n':
            roll_dice()
        else:
            print("I'm sorry but that is an incorrect submission. Please type 'Y' for yes or 'N' for no.")
    else:
        print("I'm sorry but that is an incorrect submission. Please type 'Y' for yes or 'N' for no.")

while 
