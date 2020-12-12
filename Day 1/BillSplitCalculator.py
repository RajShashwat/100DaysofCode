print("Welcome to the Bill Split Calculator!!! ")

Bill = int(input("What is the total Bill?\n"))
People = int(input("How many people to split the bill?\n"))
Tip = int(input("What percent Tax/Tip you have to pay?\n"))

split = (Bill + ((Bill*Tip)/100))/People

print("Each person has to pay: ", split)