# Number Guesser Game

This is a simple number guessing game written in Python. The computer generates a random number between 1 and 100, and the player has to guess it.  The player starts with a score of 100, and 10 points are deducted for each incorrect guess. The game ends when the player guesses the correct number or quits.

## How to Play

1.  Clone the repository to your local machine:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)  # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd NumberGuesser
    ```
3.  Run the game:
    ```bash
    python number_guesser.py
    ```
4.  Enter your guess when prompted.
5.  The game will tell you if your guess is too high or too low.
6.  To quit the game, type 'q' and press Enter.

## Game Rules

*   The computer generates a random integer between 1 and 100 (inclusive).
*   You start with a score of 100.
*   For each incorrect guess, your score decreases by 10 points, down to a minimum of 0.
*   The game ends when you guess the correct number or choose to quit.
*   Your final score is displayed when you win.

## Code Explanation

The code is structured as follows:

*   `validate_input(user_guess)`: This function checks if the user's input is a valid integer between 1 and 100. It returns `True` if the input is valid, and `False` otherwise.  It also handles the 'q' (quit) input.
*   `main()`: This is the main function that runs the game. It generates the random number, handles user input, checks the guess, updates the score, and prints the appropriate messages.

## Example