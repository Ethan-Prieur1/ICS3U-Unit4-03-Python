#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that checks if a certain year is a leap year


def main():
    # This function is the main function

    counter = 0
    number_product = 0

    # Input
    number_as_string = input("Enter a Number Above 0: ")

    # Process & Output
    try:
        number_as_int = int(number_as_string)
        if number_as_int < 0:
            print("Enter a positive number next time.")
        else:
            for counter in range(number_as_int + 1):
                number_product = counter**2
                print("{0}^2 = {1}".format(counter, number_product))
    except Exception:
        print("That ain't no number >:(")
    print("\nDone")


if __name__ == "__main__":
    main()
