from random import randint
import turtle

print ("---Guess The Number And Win A Mystery Prize---")

def lucky_number():
    number =randint(1,10)
    guess = int (input("Pick a number between 1 -10: "))
    if number != guess:
        print ("You guessed wrong dude!")
        print (number)
        booby_prize()
    elif number == guess:
        print("Your guessed right number!")
        your_price()

def booby_prize():
    print ("You get a poke in the eye!" *10)
    lucky_number()

def your_price():
    t =turtle.Pen()
    t.forward (100)
    t.left (78)
    t.right (45)
    t.forward (66)
    t.left (78)

lucky_number ()

turtle.done ()
