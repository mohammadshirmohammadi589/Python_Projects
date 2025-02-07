# Number Guessing Game

This Python program implements a number guessing game where the player tries to guess a randomly generated number within a specific range. The game has different difficulty levels, each with a different range and number of guesses allowed.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd NumberGuessingGame
    ```
3.  Run the script:
    ```bash
    python number_guessing_game.py  # Or whatever you named your Python file
    ```

## How to Play

1.  When you run the script, you'll first be prompted to choose a difficulty level:
    *   1: Easy (1-30, 10 guesses)
    *   2: Medium (1-50, 7 guesses)
    *   3: Hard (1-100, 5 guesses)
    *   4: Iran Mode (1-1000, 1 guess)
2.  Enter the number corresponding to your desired level.  If you enter an invalid number, you'll be prompted again.
3.  Once you've selected a level, the game will generate a random number within the appropriate range.
4.  You'll then be prompted to enter your guess.
5.  The game will tell you if your guess is too low, too high, or correct.
6.  You have a limited number of guesses, depending on the difficulty level.
7.  If you guess the correct number, you win!
8.  If you run out of guesses, the game will reveal the number and you lose.
9.  At the end, the game will display the number and a thank you message.

## Code Explanation

*   The code first prompts the user to select a difficulty level. Input validation is performed to ensure the user enters a valid level number.
*   Based on the selected level, the lower bound (L), upper bound (U), and the number of allowed guesses (`COUNT_GUESS`) are set.
*   A random number (`computer_guess`) is generated between L and U (inclusive).
*   The game then enters a loop that allows the user to make guesses.
*   Inside the loop, the user is prompted to enter a guess. Input validation is performed to ensure the guess is within the valid range.
*   The user's guess is compared to the computer's guess.  Feedback is provided to the user (too low, too high, or correct).
*   The loop continues until the user guesses correctly or runs out of guesses.
*   Finally, the computer's number is revealed, and a thank you message is displayed.


## License
 MIT License
