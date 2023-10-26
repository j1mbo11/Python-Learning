import random

game = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors."))

computer_choice = random.randint(0, 2)
print(f"Computer choose {game[computer_choice]}")

final_user_choice = game[user_choice]
final_computer_choice = game[computer_choice]

if final_user_choice == 'Rock' and final_computer_choice == 'Rock':
    print("Draw!")
elif final_user_choice == 'Rock' and final_computer_choice == 'Paper':
    print("Computer wins!")
elif final_user_choice == 'Rock' and final_computer_choice == 'Scissors':
    print("User Wins!")
elif final_user_choice == 'Paper' and final_computer_choice == 'Rock':
    print("User Wins!")
elif final_user_choice == 'Paper' and final_computer_choice == 'Paper':
    print("Draw!")
elif final_user_choice == 'Paper' and final_computer_choice == 'Scissors':
    print("Computer wins!")
elif final_user_choice == 'Scissors' and final_computer_choice == 'Rock':
    print("Computer wins!")
elif final_user_choice == 'Scissors' and final_computer_choice == 'Paper':
    print("User wins!")
else:
    print("Draw!")






