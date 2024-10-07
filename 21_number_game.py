def check(xyz):
    i = 1
    while i < len(xyz):
        if xyz[i] - xyz[i-1] != 1:
            return False
        i =i + 1
    return True


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
                    if 0<inp<=3:
                        comp = 4 - inp
                    else:
                        print("wrong choice. you disqualified from the game")
                        lose()

                    print("Your turn")
                    print("Enter your values")
                    i,j = 1,1

                    while i <= inp:
                        a = int(input("<"))
                        xyz.append(a)
                        i =i + 1

                    last = xyz[-1]

                    if check(xyz) == True :
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


        if chance == "S":













game = True
while game == True:
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
