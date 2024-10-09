def check(xyz):
    i = 1
    while i < len(xyz):
        if xyz[i] - xyz[i-1] != 1:
            return False
        i = i + 1
    return True


def nearest_multiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near


def lose():
    print("You lose")
    print("Better Luck Next Time")
    exit()


def start_game():
    xyz = []
    last = 0
    while True:
        print("Enter F to take the first chance")
        print("Enter S to take the second chance")
        chance = input("<")
        if chance == "F":
            while True:
                if last == 20:
                    lose()
                else:
                    print("Your turn")
                    print("How many numbers do you want to enter?")
                    inp = int(input("<"))
                    if 0 < inp <= 3:
                        comp = 4 - inp
                    else:
                        print("wrong choice. you disqualified from the game")
                        lose()

                    print("Your turn")
                    print("Enter your values")
                    i, j = 1, 1

                    while i <= inp:
                        a = int(input("<"))
                        xyz.append(a)
                        i = i + 1

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            lose()
                        else:
                            while j <= comp:
                                xyz.append(last + j)
                                j = j + 1
                            print("Order of inputs after computer's turn :")
                            print(xyz)
                            last = xyz[-1]

                    else:
                        print("you did not input consecutive integers")
                        lose()
        elif chance == "S":
            xyz = []
            last = 0
            comp = 1
            while last < 20:
                j = 1
                while j <= comp:
                    xyz.append(j + last)
                    j = j + 1
                print("Order of inputs after computer's turn :")
                print(xyz)
                if xyz[-1] == 20:
                    lose()
                else:
                    print("Your turn")
                    inp = int(input("How many numbers do you want to enter?"))
                    i = 1
                    print("Enter your values")
                    while i <= inp:
                        a = int(input(">"))
                        xyz.append(a)
                        i = i + 1
                    last = xyz[-1]
                    if check(xyz):
                        near = nearest_multiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                        else:
                            comp = comp

                    else:
                        print("you did not enter consecutive integers")
                        lose()
            print("Congratulations")
            print("You won")
            exit()

        else:
            print("wrong choice")


game = True
while game:
    print("Player 2 is computer \n")
    print("Do you want to play the 21 number game?(yes/no)")
    ans = input("<")
    if ans == "yes":
        start_game()
    else:
        print("Do you want to quit the game?")
        ans = input("<")
        if ans == "yes":
            print("you are quitting the game")
            exit()
        elif ans == "no":
            print("continuing")
        else:
            print("wrong choice")
