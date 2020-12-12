import random

print("Welcome to the Coin Tossing Program")

coin = random.randint(0,1)

if coin == 0:
    print("HEADS")
else:
    print("TAILS")