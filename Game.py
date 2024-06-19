import random

def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'stone'):
        return 'user'
    else:
        return 'computer'

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose stone, paper, or scissors: ").lower()
        if user_choice not in ['stone', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == 'user':
            print("You win!")
            user_score += 1
        elif winner == 'computer':
            print("You lose!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {user_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
