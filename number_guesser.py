
import random

def validate_input(user_guess):
    if not user_guess.isdigit():
        print("invalid number,try again")
        return False
    user_guess=int(user_guess)
    if user_guess>100 or user_guess<1:
        print("valid enter,try again:")
        return False
    return True


def main():
    rand_num=random.randint(1,100)
    score=100

    while True:
        user_guess=input("enter a number :")

        if user_guess=="q":
            print("tanks you goodby")
            break

        if not validate_input(user_guess):
            continue

        user_guess =int(user_guess)

        if rand_num > user_guess:
            print("your guess is too low.pleas try again")
        elif rand_num < user_guess:
            print("your guess is too high.pleas try again")
        else:
            print("your guess the correct number")
            print("your score is:{score}")
            break
        score -=10
        score =max(score,0)


if __name__=="__main__":
    main()

