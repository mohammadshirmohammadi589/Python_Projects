# Product Management System

This Python program demonstrates a simple product management system using inheritance. It defines a base `Product` class and two subclasses: `Book` and `Laptop`.  It showcases how to create objects of these classes, access their attributes, and use methods, including applying discounts.

## How to Run

1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://www.google.com/search?q=https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git) # Replace with your repo URL
    ```
2.  Navigate to the project directory:
    ```bash
    cd ProductManagement
    ```
3.  Run the script:
    ```bash
    python product_management.py  # Or whatever you named your Python file
    ```

## How to Use

The program is designed for demonstration. When you run it, it will:

1.  Create a `Product` object (`p1`).
2.  Print the attributes of `p1` using `vars(p1)`.
3.  Create a `Book` object (`b1`).
4.  Print the `pages` and `author` attributes of `b1`.
5.  Print the attributes of `b1` using `vars(b1)`.
6.  Print the string representation of `b1` (using the `__str__` method).
7.  Call the `show_name()` method for both `b1` and `p1`.  *(Note:  `p1` will raise an AttributeError because the `Product` class does not have a `show_name` method. This is an example of how subclasses can have methods that the parent class does not.)*

You can modify the code within the `if __name__ == "__main__":` block to create more `Product`, `Book`, and `Laptop` objects, test the `apply_discount()` method, and explore other functionalities.

## Code Explanation

*   **`Product` Class:**
    *   `__init__(self, name, price, category)`: The constructor initializes a `Product` object with a name, price, and category.
    *   `__str__(self)`: Returns a string representation of the product.
    *   `show_price()`: Prints the price of the product.
    *   `apply_discount(self, value)`: Applies a discount to the product's price.  Raises a `ValueError` if the discount value is not between 0 and 100.

*   **`Book` Class (Inherits from `Product`):**
    *   `__init__(self, name, price, category, author, pages)`: The constructor initializes a `Book` object with the attributes of a `Product` and adds `author` and `pages` attributes.  It calls the parent class's `__init__` using `super().__init__()`.
    *   `__str__(self)`: Overrides the parent class's `__str__` method to include the author and page count.
    *   `show_name()`: Prints the name of the book.

*   **`Laptop` Class (Inherits from `Product`):**
    *   `__init__(self, name, price, category, processor, ram)`: The constructor initializes a `Laptop` object, adding `processor` and `ram` attributes.
    *   `__str__(self)`: Overrides the parent class's `__str__` method to include the processor and RAM.


## License
 MIT License
