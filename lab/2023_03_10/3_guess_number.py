# GUESS THE NUMBER
# with while

import random

secret = random.randint(1, 100)  # genera numero intero randomico tra 1 e 100

i = 1
while i < 6 :
    print("Attempt number", i)
    guess = int(input("enter a number: "))  # to convert form string to number

    if secret == guess:
      print("you won!")
      break     # immediately exit for loop if I guess the rigth number
    elif secret < guess:
        print("too large")
    else:
        print("too small")
    i += 1

if secret != guess:
    print("YOU LOST!!!")
    print("Right answer was", secret)





