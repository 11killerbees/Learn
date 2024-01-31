import time
import random
class Cords:
    def __init__(self, name, placement):
        self.name = name
        self.placement = placement

    def __str__(self):
        return "   "+self.name + self.placement

def randCords(list,interval,total):

    total=total

    rep =-1
    here = True

    for i in range(total):
        while here:
            num = random.randint(0,len(list)-1)
            if num == rep:
                print()
            else:
                here = False
                rep = num


        here = True
        print(list[num])
        print("\n\n\n\n\n\n\n")
        time.sleep(interval)
        print("\n\n\n\n\n\n\n")
    return





"Am","C","F","G"

Am = Cords("Am", "\n  O O O"
                                "\n| | | |"
                                "\nX | | |"
                                "\n| | | |"
                                "\n| | | |")

C = Cords("C",   "\nO O O"
                                "\n| | | |"
                                "\n| | | |"
                                "\n| | | X"
                                "\n| | | |")

F = Cords("F",   "\n  O   O"
                                "\n| | X |"
                                "\nX | | |"
                                "\n| | | |"
                                "\n| | | |")

G = Cords("G",   "\nO     "
                                "\n| | | |"
                                "\n| X | X"
                                "\n| | X |"
                                "\n| | | |")

D = Cords("D",   "\n      O"
                                "\n| | | |"
                                "\nX X X |"
                                "\n| | | |"
                                "\n| | | |")

eazy = [Am,C,F,G,D]


randCords(eazy,2,50)