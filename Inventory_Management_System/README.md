# Inventory Management System

This Python program implements a basic inventory management system. It allows you to add, remove, display, edit, and search for items in an inventory.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd InventoryManagement
    ```
3.  Create the `item.py` file. This file should contain the definition of the `item` class. See the "Item Class (`item.py`)" section below for the required code.
4.  Run the script:
    ```bash
    python inventory_manager.py  # Or whatever you named your Python file
    ```

## How to Use

The program is currently designed for demonstration and testing.  The `if __name__ == "__main__":` block contains example code that shows how to use the `InventoryManager` class.  You would need to modify this section to create an interactive menu or integrate with a user interface (like Tkinter or Streamlit) to make it more user-friendly.

Here's a breakdown of how the example code works:

1.  `m1 = InventoryManager()`: Creates an instance of the `InventoryManager` class.
2.  `item1 = m1.create_item("1", "B", 3, 200)`: Creates a new item with ID "1", name "B", quantity 3, and price 200.
3.  `item2 = m1.create_item("2", "B", 3, 200)`: Creates another item.
4.  `m1.add_item(item1)` and `m1.add_item(item2)`: Adds the items to the inventory.
5.  `m1.display_item()`: Displays all items in the inventory.
6.  `m1.edit_item("1")`: Edits the item with ID "1".  You'll be prompted to enter new values for the name, price, and quantity.  Pressing Enter without typing anything will keep the existing value.
7.  `m1.display_item()`: Displays the updated inventory.
8.  `m1.search("B")`: Searches for items with the name "B".
9.  `m1.details()`: Displays the number of products and the total price of all items in the inventory.

You can modify the code within the `if __name__ == "__main__":` block to test other functionalities (like removing items).
