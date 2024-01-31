import random
nums = {1:"ichi",
        2:"ni",
        3:"san",
        4:"shi",
        5:"go",
        6:"roku",
        7:"nana",
        8:"hachi",
        9:"kyuu",
        10:"jyuu",}

for i in range (0,25):

        answer = nums[random.randint(1,10)]
        num = random.randint(1,len(nums))
        print(num)
        check = input("")
        check.lower()
        if check == nums[num]:
                print("right")
        else:
                print("wrong")

