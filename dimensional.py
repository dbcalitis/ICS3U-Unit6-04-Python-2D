#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Oct 2021
# This program determines the average

import random


def mean(num_array):
    # This function determines the average of the 2D array
    num_rows = len(num_array)
    num_columns = len(num_array[0])
    average = 0

    for row in range(num_rows):
        for column in range(num_columns):
            average += num_array[row][column]

    average = round(average / (num_rows * num_columns), 2)

    return average


def main():
    # This function is the main function
    main_array = []

    try:
        # input & process
        user_rows = input("How many rows would you like: ")
        user_rows = int(user_rows)
        user_columns = input("How many columns would you like: ")
        user_columns = int(user_columns)

        # output
        print("")
        for row in range(user_rows):
            temp_array = []

            for column in range(user_columns):
                random_number = random.randint(0, 50)
                temp_array.append(random_number)
                if random_number >= 10:
                    print("{0} ".format(random_number), end="")
                else:
                    print("{0}  ".format(random_number), end="")

            main_array.append(temp_array)
            print("")

        print("\nThe average of all the numbers is: {0}".format(mean(main_array)))
    except (Exception):
        print("\nInvalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
