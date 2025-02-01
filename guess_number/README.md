This is a simple number guessing game implemented using Python's Tkinter library for the graphical user interface. The player guesses a number between 1 and 100, and the game provides feedback.

How to Run
Clone the repository:
git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
Navigate to the project directory:
cd NumberGuessingGameTkinter
Run the script:
python number_guessing_game.py  # Or whatever you named your Python file
# How to Play
The game window will appear.
Enter your guess in the entry box.
Click the "حدس بزن" (Guess) button.
The game will display your guess. (Currently, the game only displays the user's guess. It needs to be improved to provide feedback on whether the guess is too high, too low, or correct.)
Click the "خروج" (Exit) button to close the game. (Currently, the Exit button doesn't have any functionality. It needs to be connected to the window's close event.)
# Code Explanation
The code uses the tkinter library to create the GUI.
LOWER and UPPER constants define the range for the secret number (1 to 100).
guessnumber() function is called when the "Guess" button is clicked. (This function currently only prints the entered number and displays it back to the user. It needs to be updated to handle the game logic - comparing the guess to the secret number and providing feedback.)
The code creates labels, an entry box for user input, and buttons for "Guess" and "Exit".
The window.mainloop() starts the Tkinter event loop, making the GUI interactive.

# Requirements
Python 3.x (with the tkinter library, which is usually included with Python)
# License
MIT License
