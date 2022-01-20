from random import randint
count = 0
randNum = randint(0,1001)
guess = int(input("See if you can guess the number I'm thinking, between 0 and 1000: "))
while guess != randNum:
    count = count +1
    if guess < randNum:
        print("Try higher!")
    else:
        print("Lower! Try again.")
    guess = int(input(": "))
print( "You got it! Only took you", count, "tries. ;-)" )
