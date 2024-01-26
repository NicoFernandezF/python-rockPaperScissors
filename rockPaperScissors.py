rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# 0 rock, 1 paper, 2 scissors
import random

player_score = 0
computer_score = 0
choices = [rock, paper, scissors]
while (player_score < 3) and (computer_score < 3):
    player_choice = int(
        input("Please type 0 for rock, 1 for paper, or 2 for scissors\n")
    )
    computer_choice = random.randint(0, 2)

    print(f"you chose\n{choices[player_choice]}")
    print(f"the computer chose\n{choices[computer_choice]}")

    if player_choice == computer_choice:
        print("it's a tie!")
    elif player_choice == 0:
        if computer_choice == 1:
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    elif player_choice == 1:
        if computer_choice == 0:
            print("You win!")
            player_score += 1
        else:
            print("You lose!")
            computer_score += 1
    elif player_choice == 2:
        if computer_choice == 0:
            print("You lose!")
            computer_score += 1
        else:
            print("You win!")
            player_score += 1
    print(f"Your score is {player_score} and the computer is {computer_score}\n")
if player_score == 3:
    print("Congratulations, you beat the computer")
elif computer_score == 3:
    print("Sorry, the computer won this time!")
