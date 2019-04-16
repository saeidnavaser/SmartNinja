#import random
from random import  randint

#secret = random.randint(0, 30)

#while True:
   # guess = int(input("Guess the secret number (between 1 and 30): "))

   # if guess == secret:
   #     print("You've guessed it - congratulations! It's number " + str(secret))
   #     break
  #  elif guess > secret:
    #    print("Your guess is not correct... try something smaller")
  #  elif guess < secret:
    #    print("Your guess is not correct... try something bigger")


while True:
    print('change Km to Mi')

    km = float(input ('kilometer:'))
    miles = km * 0.62

    print(miles)

    user = input('try again? y/n')

    if user == "y":
        print('yes')
        continue
    if user == "n":
        print('not')
        break


