import random

def fortunelist():
    list=[
        "you are lucky to win 1 crore",
          "you will end up single",
          "you will celebrate your 100th birthday",
          "A new romance is in the future",
          "Plan for many pleasures ahead.",
          "Something you lost will turn up soon.",
          "You will soon discover yor hidden talents",
          "Soon you will receive a letter from a loved one",
          "Never do anything halfway",
          "A secret admirer will soon send you a sign of affection.",
          "A thrilling time is in your near future.",
          "Your heart is in a place to draw true happiness.",
          "The one you love is closer than you think",
          "Your heart will skip a beat.",
          "You will move to a beautiful home within a year",
          "Soon you will receive a letter from a loved one",
          "Don't go to a fortune teller, create your own future.",
          "Someone is thinking of you.",
          'Soon life will become more interesting.'
          "New ideas could be profitable",
          "You will have good luck today!"


    ]
    return random.choice(list)

def play(start):
    if start in yes:
        try:
            num = int(input("enter a number:  "))
            print(fortunelist())

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


    else:
        print("enter yes to play :) OR ")
        ex = input('enter 1 to exit ')
        if ex == '1':
            exit()
        else:
            play(ex)

while(True):
    start = input("Do you want to play the game?\n 1.yes \n 2.no ")
    yes=['YES','yes','Yes','YEs','yES','yeS','YeS','yEs']
    play(start)

play()