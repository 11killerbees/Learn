import random

digit1 = {
        0:"",
        1:"ichi",
        2:"ni",
        3:"san",
        4:"shi",
        5:"go",
        6:"roku",
        7:"nana",
        8:"hachi",
        9:"kyuu",}

digit2 = {
        0:"",
        1:"ju ",
        2:"ni ju ",
        3:"san ju ",
        4:"shi ju ",
        5:"go ju " ,
        6:"roku ju ",
        7:"nana ju ",
        8:"hachi ju ",
        9:"kyuu ju " ,}

digit3 = {
        0:"",
        1:"hyaku ",
        2:"ni hyaku ",
        3:"san hyaku ",
        4:"shi hyaku ",
        5:"go hyaku " ,
        6:"roku hyaku ",
        7:"nana hyaku ",
        8:"hachi hyaku ",
        9:"kyuu hyaku " ,}

for i in range(1,10):
        base1 = random.randint(0,9)
        base2 = random.randint(0,9)
        base3 = random.randint(0,9)
        num = int(str(base3)+str(base2)+str(base1))
        d1 = digit1[base1]
        d2 = digit2[base2]
        d3 = digit3[base3]
        text = d3+d2+d1
        print("\n",text)
        check = input("type the number ")
        if int(check) == int(num):
                print("right")
                print("num is",num)
        else:
                print("wrong")
                print("answer was", num)


