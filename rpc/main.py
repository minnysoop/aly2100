# ROCK, PAPER, SCISSORS
# Import necessary modules
import random
from datetime import datetime

# Creating a game class
class Game:
    # For every game, we have
    def __init__(self):
        # a winner
        self.winner = ''
        # a player's move
        self.player_move = ''
        # a computer's move
        self.computer_move = ''

# Entry function
def main():
    # Introduction Text
    print("Let's Play Rock, Paper, Scissors! \n")
    print("This game saves your history in the file called game_history.txt\n")
    # Creates a new file containing game history
    try:
        history = open("game_history.txt", "x")
    except FileExistsError:
        history = open("game_history.txt", "a")
    # Get current date time
    now = datetime.now()
    # Adding a title to the history file
    history.write("\nGAME HISTORY: " + str(now) + "\n")
    # Represents the numebr of games played
    games_played = 1
    # Represents if a game is ongoing 
    game_on = True
    # While there is an ongoing game
    while game_on:
        # Create game object
        current_game = Game()
        # List of possible moves
        possible_moves = ['rock', 'paper', 'scissors']
        # Prompt user for a move
        player_move = input("Enter a move: ").lower()
        # Check validity
        while not valid(player_move):
            player_move = input("Enter a move: ").lower()
        # Update current game object
        current_game.player_move = player_move
        # Generate computer move 
        computer_move = possible_moves[random.randint(0, 2)]
        # Update current game object
        current_game.computer_move = computer_move
        print('Computer\'s move: ' + computer_move)
        # Evaluate winner
        winner = evaluate_winner(player_move, computer_move)
        # Update current game object
        current_game.winner = winner
        print('Winner: ' + winner)

        # Update game history file
        history.write('-------------------------'  + '\n')
        history.write('GAME #' + str(games_played) + '\n')
        history.write('PLAYER MOVE: ' + current_game.player_move  + '\n')
        history.write('COMPUTER MOVE: ' + current_game.computer_move  + '\n')
        history.write('WINNER: ' + current_game.winner + '\n')

        # Ask use if they want to continue playing
        continue_playing = input("Continue Playing? (Y/N): ")
        while not (continue_playing == 'Y' or continue_playing == 'N'):
            continue_playing = input("Continue Playing? (Y/N): ")
        if continue_playing == 'N':
            break
        else:
            games_played += 1
    

# Checks if a player's move is valid
def valid(player_move):
    # If the player inputs any one of these guesses
    if player_move == 'rock' or player_move == 'paper' or player_move == 'scissors':
        # Return true
        return True
    # Return false if all else fails
    return False

# Evaluate winner
def evaluate_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'DRAW'
    elif player_move == 'rock' and computer_move == 'paper':
        return 'COMPUTER'
    elif player_move == 'rock' and computer_move == 'scissors':
        return 'PLAYER'
    elif player_move == 'paper' and computer_move == 'rock':
        return 'PLAYER'
    elif player_move == 'paper' and computer_move == 'scissors':
        return 'COMPUTER'
    elif player_move == 'scissors' and computer_move == 'rock':
        return 'COMPUTER'
    elif player_move == 'scissors' and computer_move == 'paper':
        return 'PLAYER'
    
main()
