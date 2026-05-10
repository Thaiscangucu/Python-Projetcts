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

choice = int(input("What do you chooes? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer = random.randint(0, 2)

#user choice:
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
else:
  print(scissors)

#computer choice:
print("\nComputer chose: \n")
if computer == 0:
  print(rock)
elif computer == 1:
  print(paper)
else:
  print(scissors)
  
#rules:
if choice >= 3 or choice < 0: 
  print("You typed an invalid number, you lose!")

elif choice == 0 and computer == 2:
  print("You win!")

elif computer == 0 and choice == 2:
  print("You lose!")

elif computer > choice:
  print("You lose!")

elif choice > computer:
  print("You win!")

elif computer == choice:
  print("It's a draw!")