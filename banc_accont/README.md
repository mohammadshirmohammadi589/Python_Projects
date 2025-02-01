# Bank Account Management System

This Python program simulates a basic bank account management system. It allows users to create accounts, view balances, deposit money, and withdraw money.  It includes a simple command-line interface.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd BankAccountManagement
    ```
3.  Run the script:
    ```bash
    python bank_account.py  # Or whatever you named your Python file
    ```

## How to Use

1.  When the script starts, an account is automatically created for "mohammad shirmohammadi".  The account number is displayed, and the initial balance is 0.
2.  You'll see a menu with the following options:
    *   1: View your balance
    *   2: Deposit money
    *   3: Withdraw money
    *   4: Exit
3.  Enter the number corresponding to your choice and press Enter.
4.  If you choose to deposit or withdraw, you'll be prompted to enter the amount.
5.  The program will display the updated balance after each transaction.
6.  To exit the program, enter 4.

## Code Explanation

*   **`BANCACCONT` Class:**
    *   `all_accont_numbers`: A class-level set to store all account numbers, ensuring each account has a unique number.
    *   `last_accont_number`: A class-level variable that keeps track of the last assigned account number.
    *   `__init__(self, name)`: The constructor initializes a new account. It takes the account holder's name as input, assigns a unique account number, and sets the initial balance to 0.
    *   `display()`: Displays the account holder's name and current balance.
    *   `deposit()`: Allows the account holder to deposit money.
    *   `withdraw()`: Allows the account holder to withdraw money.  It checks if there are sufficient funds before processing the withdrawal.
# Licence
MIT
