Happy Numbers
In this python project, you'll be diving into the world of "happy" numbers. A number is considered "happy" if by following a specific sequence, it results in 1. The sequence is as follows: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. These numbers for which this process ends in 1 are happy numbers.

For example, 19 is a happy number. Here's why:

1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
As you can see, we eventually reached 1, which makes 19 a "happy" number. This project tasks you with creating a program that can accurately determine whether any given positive integer is a happy number or not.

Project Structure
README.md
requirements.txt
src/
    happy_number.py
Requirements
Python 3.7+
A basic understanding of Python and its core concepts
Learning Outcomes
This project will help you practice:

Using Python's core functionality, such as lists, loops, and sets, to solve a complex problem.
Incorporating mathematical concepts in a programming environment.
Writing and running unit tests to ensure that your code is working as intended.
Improve your problem-solving abilities and debugging skills
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1


if __name__ == "__main__":
    assert is_happy(19), 'Test Case 1 Failed'
    assert not is_happy(2), 'Test Case 2 Failed'
    assert is_happy(44), 'Test Case 3 Failed'
    assert is_happy(86), 'Test Case 4 Failed'
    assert is_happy(139), 'Test Case 5 Failed'

    print('All test cases pass')
