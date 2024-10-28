# user_input = int(input("enter a number"))
# n = range(20)
# if user_input % 2 != 0:
#     print("weird")
# if user_input % 2 == 0 and >=2 <=5:
#     print("Not Weird")
# elif user-input % 2 == 0 and >=6 <=20:
#     print("Weird")
# elif user_input % 2 == 0 and > 20:
#     print("Not weird")

# names = ["jidenyms", "timi" ,"divine" ,"micheal"]
# namess = ["nymous", "anonymous", "nyms"]
# names.extend(namess)
# names[3] = "lara"
# names[5] = "tolu"
# print(names)

import random
rad = random.randint(1,100)

while True:
    user_input = int(input("enter a random number: "))
    if user_input == rad:
        print("guess right")
        break
    elif user_input > rad and user_input <= 100:
        print("your guess is high ")

    elif user_input < rad and user_input >= 1:
        print("guess is low")
    elif user_input < 1 or user_input > 100:
        print('out of range')
    else:
        ("invalid syntax")


