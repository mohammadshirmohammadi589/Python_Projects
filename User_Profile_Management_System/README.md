# User Profile Management System

This Python program implements a user profile management system. It allows users to create profiles, log in, log out, update their email and password, view their activity logs, and provides some statistics about users.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd UserProfileManagement
    ```
3.  Run the script:
    ```bash
    python user_profile.py  # Or whatever you named your Python file
    ```

## How to Use

The program is currently designed for demonstration and testing.  It's not set up for interactive use in its current state.  The `if __name__ == "__main__":` block contains example code that demonstrates how to create users, log in, update information, and use other features.  You would need to modify this section to create an interactive menu or integrate with a user interface (like Tkinter or Streamlit) to make it more user-friendly.

Here's a breakdown of how the example code works:

1.  `user1 = UserProfile("abc", "123", "a.b@gmail.com", 17)`: Creates a new user profile with the username "abc", password "123", email "a.b@gmail.com", and age 17.
2.  `print(user1.email)`: Prints the user's email.
3.  `user1.login("abc", "123")`: Logs in the user.
4.  `user1.update_email("a.c")`: Attempts to update the user's email.  This will raise a `ValueError` because "a.c" is not a valid email format.
5.  `print(user1.email)`: Prints the user's email (which will not have been updated due to the error).
6.  `print(user1.is_valid_email("a.b@gmail.com"))`: Demonstrates how to use the `is_valid_email` static method to check if an email is valid.

You can modify the code within the `if __name__ == "__main__":` block to test the other functionalities (logout, change password, show logs, etc.).

## Code Explanation

*   **`UserProfile` Class:**
    *   `user_count`: A class-level variable to count the total number of users.
    *   `logged_in_users`: A class-level variable to count the number of logged-in users.
    *   `logged_out_users`: A class-level variable to count the number of logged-out users.
    *   `__init__(self, username, password, email, age)`: The constructor to initialize a new user profile.  It takes the username, password, email, and age as input.  It also validates the email address using the `is_valid_email` static method.
    *   `login(self, username, password)`: Logs in the user if the provided credentials are correct.  Updates the `is_login` status and adds a log entry.
    *   `logout()`: Logs out the user.  Updates the `is_login` status and adds a log entry.
    *   `update_email(self, new_email)`: Updates the user's email.  Validates the new email address before updating.
    *   `change_pass(self, new_pass)`: Changes the user's password.
    *   `show_logs()`: Displays the user's activity logs.
    *   `display()`: Displays the user's profile information.
    *   `number_of_users()` (class method): Displays the total number of users, the number of logged-in users, and the number of logged-out users.
    *   `is_valid_email()` (static method): Checks if a given email address is valid.


## License

 MIT License
