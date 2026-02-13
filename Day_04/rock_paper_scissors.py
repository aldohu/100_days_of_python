import random
positions = ["rock", "paper", "scissors"]   

print("Welcome to Rock, Paper, Scissors!")

computer_score =random.randint(0, 2)
user_score = input("Type 'rock', 'paper', or 'scissors' to play.")


if user_score == positions[computer_score]:
    print("It's a tie!")
elif user_score == "rock" and positions[computer_score] == "scissors":
    print("You win! Rock crushes scissors.")
elif user_score == "paper" and positions[computer_score] == "rock":
    print("You win! Paper covers rock.")
elif user_score == "scissors" and positions[computer_score] == "paper":
    print("You win! Scissors cut paper.")
else:
    print(f"You lose! {positions[computer_score].capitalize()} beats {user_score}.")