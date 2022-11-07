#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Nov. 6, 2022
# This program asks for a number
# and shows the powers of all
# numbers leading up to it

import math


def main():
    # introductory paragraph
    print("This program asks for a number")
    print("and shows the powers of all")
    print("numbers leading up to it")
    print("")

    # input
    # getting user_num_string
    user_num_string = input("Enter a positive number: ")

    # initializing counter
    counter = 0

    # process
    # checking that user_num_string is an integer
    try:
        user_num_int = int(user_num_string)

        if user_num_int >= 0:
            # initializing user_num_plus
            user_num_plus = user_num_int + 1

            for counter in range(0, user_num_plus):
                # updating power
                power = counter**2
                # printing output
                print(("{}^2 = ").format(counter))
                print(power)
                # updating counter
                counter = counter + 1
        else:
            print("Please enter a positive, whole integer.")
    except ValueError:
        print("Please enter a valid integer.")
    finally:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
