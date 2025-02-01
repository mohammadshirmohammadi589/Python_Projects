# Number Guessing Game (Tkinter)

This is a simple number guessing game implemented using Python's Tkinter library for the graphical user interface. The player guesses a number between 1 and 100, and the game provides feedback.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd NumberGuessingGameTkinter
    ```
3.  Run the script:
    ```bash
    python number_guessing_game.py  # Or whatever you named your Python file
    ```

## How to Play

1.  The game window will appear.
2.  Enter your guess in the entry box.
3.  Click the "حدس بزن" (Guess) button.
4.  The game will display your guess.  *(Currently, the game only displays the user's guess.  It needs to be improved to provide feedback on whether the guess is too high, too low, or correct.)*
5.  Click the "خروج" (Exit) button to close the game. *(Currently, the Exit button doesn't have any functionality. It needs to be connected to the window's close event.)*

## Code Explanation

*   The code uses the `tkinter` library to create the GUI.
*   `LOWER` and `UPPER` constants define the range for the secret number (1 to 100).
*   `guessnumber()` function is called when the "Guess" button is clicked.  *(This function currently only prints the entered number and displays it back to the user. It needs to be updated to handle the game logic - comparing the guess to the secret number and providing feedback.)*
*   The code creates labels, an entry box for user input, and buttons for "Guess" and "Exit".
*   The `window.mainloop()` starts the Tkinter event loop, making the GUI interactive.

## Improvements Needed (Important!)

This game is very basic and needs significant improvements to be fully functional:

*   **Game Logic:**  The most important missing piece is the actual game logic.  The `guessnumber()` function needs to:
    *   Generate a random secret number.
    *   Compare the user's guess to the secret number.
    *   Provide feedback to the user (e.g., "Too high!", "Too low!", "You got it!").
*   **Exit Button Functionality:** The "Exit" button should be connected to the `window.quit()` or `window.destroy()` method to close the application.
*   **Input Validation:** You should add input validation to ensure the user enters a valid number (an integer within the specified range).  Handle potential errors (e.g., non-numeric input).
*   **Number of Attempts:**  Consider limiting the number of attempts the user has.
*   **Score:**  You could add a scoring system.
*   **Clearer UI:** The UI could be made more user-friendly with better layout and feedback.

## Requirements

*   Python 3.x (with the `tkinter` library, which is usually included with Python)

## License

 MIT License]
