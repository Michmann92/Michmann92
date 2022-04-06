name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose.')

elif answer == "right":
    answer = input("You have come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You crossed the bridge and encountered a snake on the way, ignore it or kick it off? (ignore/kick)? ")
        if answer == "ignore":
            print("Snake bit you and you died instantly")
        elif answer == "kick":
            print("You made it across and found civilization, You win the game!")
    else:
        print("not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print("Thank you for trying my game " + name + "!")

