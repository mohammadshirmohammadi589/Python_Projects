# Monty Hall Problem Simulator (Streamlit)

This Python application uses Streamlit to simulate the Monty Hall problem and visualize the win probabilities for switching doors versus staying with the initial choice.



## How to Use

1.  The Streamlit app will open in your web browser.
2.  You'll see a title image (presumably `banner.png`).
3.  Enter the number of games you want to simulate in the number input box.
4.  The app will simulate the games and display two line charts:
    *   One chart shows the win percentage if you *don't* switch doors.
    *   The other chart shows the win percentage if you *do* switch doors.
5.  The charts will update dynamically as the simulation progresses, showing how the win percentages converge towards the theoretical probabilities.

## Code Explanation

*   **`monty_hall_app.py` (Streamlit App):**
    *   Uses `streamlit` to create the interactive web app.
    *   Takes the number of games to simulate as input from the user.
    *   Uses `st.columns` to create two columns for the charts.
    *   Creates two line charts using `st.line_chart`.
    *   Iterates through the specified number of games, simulating each game using the `simulate_games` function (from `monty_hall.py`).
    *   Updates the charts with the running win percentages after each game.
    *   Uses `time.sleep` to introduce a small delay, making the chart updates visible.

*   **`monty_hall.py` (Simulation Logic):**
    *   Contains the `simulate_games(num_games)` function, which likely implements the logic of the Monty Hall problem simulation.  This function should:
        *   Simulate the specified number of games.
        *   For each game, randomly choose the door with the car, the player's initial choice, and the door revealed by the host.
        *   Calculate whether the player wins or loses for both the "switch" and "no-switch" strategies.
        *   Return the number of wins for each strategy.

# Licence

MIT
