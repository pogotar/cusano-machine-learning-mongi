# GUESS THE NUMBER
# with for

import random

secret = random.randint(1, 100)  # genera numero intero randomico tra 1 e 100


for i in range(5):
    print("Attempt number", i)
    guess = int(input("enter a number: "))  # to convert form string to number

    if secret == guess:
      print("you won!")
      break     # immediately exit for loop if I guess the rigth number
    elif secret < guess:
        print("too large")
    else:
        print("too small")

if secret != guess:
    print("YOU LOST!!!")
    print("Right answer was", secret)





