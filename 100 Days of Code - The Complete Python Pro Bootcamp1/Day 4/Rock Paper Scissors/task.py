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
print("lets play roct paper scissor with the computer let get who wins ")
user_input = int(input("what you wanna choose 0 : rock , 1 : paper , 2 : scissors "))
if user_input == 0:
    print("you chose rock"+rock)
elif user_input == 1:
    print("you chose paper"+paper)
else:
    print("you chose scissors"+scissors)
list = [rock,paper,scissors]
computer = random.choice(list)
print("computer hase choosen " + computer)
if user_input == computer:
    print("match draw")
elif user_input == 0 and computer ==paper:
    print("you lose")
elif user_input == 0 and computer ==scissors:
    print("you win")
elif user_input == 1 and computer ==rock:
    print("you win")
elif user_input == 1 and computer ==scissors:
    print("you lose")
elif user_input == 2 and computer ==paper:
    print("you win")
elif user_input == 2 and computer ==rock:
    print("you lose")