# write ' hello world' in the browser
import random

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'It\'s a tie!'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return 'You win!'
    else:
        return 'You lose!'

def main():
    player_score = 0
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        choices = ['rock', 'paper', 'scissors']
        computer_choice = random.choice(choices)
        
        if player_choice in choices:
            result = play_game(player_choice, computer_choice)
            print(f"Computer chose {computer_choice}. {result}")
            
            if result == 'You win!':
                player_score += 1
            elif result == 'You lose!':
                player_score -= 1
                
            print(f"Your score: {player_score}")
            
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

if __name__ == "__main__":
    main()

def main():
    player_score = 0
    
    while True:
        player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        
        if player_choice in ['rock', 'paper', 'scissors']:
            result = play_game(player_choice)
            print(f"Computer chose {computer_choice}. {result}")
            
            if result == 'You win!':
                player_score += 1
            elif result == 'You lose!':
                player_score -= 1
                
            print(f"Your score: {player_score}")
            
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

if __name__ == "__main__":
    main()
