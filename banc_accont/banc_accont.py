
from random import randrange
from typing import Set


class BANCACCONT:
    """
    bank accont management.
    """
    all_accont_numbers: Set[int] = set()
    last_accont_number = 999

    
    def __init__(self, name: str ) -> None:
        BANCACCONT.last_accont_number += 1
        an = BANCACCONT.last_accont_number
        self.accont_namber: int = an

        self.name = name
        self.balance: float = 0


    def display(self) -> None:
        """
        show accont balance.
        :return:
        """
        print(40 * "_")
        print(f"hi,{self.name}\n your current balance:{self.balance}")
        print(40 * "_")


    def deposit(self) -> None:
        """
        increase accont balance.
        :return:
        """
        amount = float(input("please enter amount to deposite:"))
        self.balance += amount
        self.display()


    def withdraw(self) -> None:
        """
        withdrow from bank accont.
        :return:
        """
        amount = float(input("please enter amount to withdraw:"))
        if amount > self.balance:
            print("insufficient balance!")

        else:
            self.balance -= amount
        self.display()
        

def main():
    print()
    acc1 = BANCACCONT("mohammad shirmohammadi")
    print(40 * "*")
    print(f"accont_namber:{acc1.accont_namber}")
    print(40 * "*")
    acc1.display()

    while True:
        choice = int(input("enter:\n 1 to see your balance,\n 2 to deposit\n"
                           "3 to withdraw,\n4 to exit.\n\t\t your choice: "))

        if choice == 1:
            acc1.display()
        elif choice == 2:
            acc1.deposit()
        elif choice == 3:
            acc1.withdraw()
        elif choice == 4:
            break
        else:
            print("please enter a valid number.")


if __name__ == "__main__":
    main()

account1 = BANCACCONT("mohammad")


account1.deposit()
account1.withdraw()












