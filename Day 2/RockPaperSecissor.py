import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_img = [rock, paper, scissors]

user_choice = int(input("What do you choose? \nEnter 0 for Rock\nEnter 1 for Paper\nENter 2 for scisssors\n"))
print("\nUser Choice")

print(game_img[user_choice])

computer_choice = random .randint(0,2)
print("Computer Choice")
print(game_img[computer_choice])

if user_choice == 0 and computer_choice == 1:
    print("You Loss")
elif user_choice == 0 and computer_choice == 2:
    print("You Win")
elif user_choice == 1 and computer_choice == 0:
    print("You Win")
elif user_choice == 1 and computer_choice == 2:
    print("You Loss")
elif user_choice == 2 and computer_choice == 1:
    print("You Win")
elif user_choice == 2 and computer_choice == 0:
    print("You Loss")
else:
    print("Draw")

