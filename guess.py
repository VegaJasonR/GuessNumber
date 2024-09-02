import random

def play_game(player_name):
    # Generate a random number for the player to guess
    number = random.randint(1, 20)
    
    print('Well ' + player_name + ', I am thinking of a number between 1 and 20.')

    # Allow the player to make up to 6 guesses
    for guessesMade in range(6):
        print('Take a guess.')
        guess = int(input())

        # Provide feedback based on the player's guess
        if guess < number:
            print('Your guess is too low!')

        if guess > number:
            print('Your guess is too high!')

        if guess == number:
            break

    # Display the outcome of the game
    if guess == number:
        guessesMade = str(guessesMade + 1)
        print('Awesome, ' + player_name + '! You guessed my number in ' + str(guessesMade) + ' guesses!')

    if guess != number:
        number = str(number)
        print('Oh no! The number I was thinking of was ' + number + '.')

# Ask for the player's name
print('Greetings! What is your name?')
player_name = input()

# Game loop to ask the player if they want to play again
play_again = 'yes'
while play_again.lower() == 'yes':
    play_game(player_name)
    print('Would you like to play again? (yes or no)')
    play_again = input()