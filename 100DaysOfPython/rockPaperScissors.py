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
import random

choices_list = ["rock", "paper", "scissors"]

#p1 human makes choice
print("Rock, paper, scissors go on 3")
p1 = input("3...2...1")

#p2 computer random choice

random_choice = random.randint(0, len(choices_list) -1)

