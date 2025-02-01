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

## `monty_hall.py` (Example Implementation - You'll need to create this file)

```python
import random

def simulate_games(num_games):
    wins_with_switching = 0
    wins_without_switching = 0

    for _ in range(num_games):
        # 1. Randomly choose the door with the car (0, 1, or 2)
        car_door = random.randint(0, 2)

        # 2. Player randomly chooses a door
        player_choice = random.randint(0, 2)

        # 3. Host reveals a door that is not the car door and not the player's choice
        available_doors = [i for i in range(3) if i != car_door and i != player_choice]
        revealed_door = random.choice(available_doors)

        # 4. Player can switch or stay
        # If switching:
        switch_choice = [i for i in range(3) if i != player_choice and i != revealed_door][0]

        # Determine wins:
        if switch_choice == car_door:
            wins_with_switching += 1
        if player_choice == car_door:
            wins_without_switching += 1
            
    return wins_with_switching, wins_without_switching
