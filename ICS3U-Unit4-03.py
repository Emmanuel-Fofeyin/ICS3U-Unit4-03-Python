#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program uses a for loop.


def main():
    # This program calculates the a positive integer squared

    # Input
    positive_string = input("Enter an integer >= 0: ")

    # Process and output
    try:
        positive_float = float(positive_string)
        positive_integer = int(positive_float)
        if positive_integer == positive_float:
            if positive_integer >= 0:
                for loop_counter in range(positive_integer + 1):
                    squared_number = loop_counter * loop_counter
                    print("{0}² = {1}".format(loop_counter, squared_number))
            else:
                print("You did not enter a positive integer.")
        else:
            print("You did not enter an integer.")
    except ValueError:
        print("You did not enter an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()