from random import *
x= str(randint(0,10000))
print ("Your Number : "+x)
y=str(randint(0,10000))
print("Lucky Number : "+y)
if x == y:
    print ("You won the game")
else:
    print("Sorry you lost the game")