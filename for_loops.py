#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 17, 2021
# Determines square of all numbers leading up to a number


def main():
    # Input

    user_input = (input("Enter your positive number: "))

    try:
        user_number = int(user_input)
        loop_counter = 0
        user_number = user_number + 1
        # Process and output
        for loop_counter in range(user_number):
            total = loop_counter * loop_counter
            print("{0}² = {1}".format(loop_counter, total))
            loop_counter = loop_counter + 1
        print("{0:,.0f} is the square of the previous numbers before {1}"
              .format(total, user_input))

    except Exception:
        print("{} is not a positive integer".format(user_input))
    finally:
        print("Done.")


if __name__ == "__main__":
    main()
