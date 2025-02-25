#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Tracks number of elements successfully printed
    try:
        # Iterate up to x times
        for i in range(x):
            # Print element at index i without newline (end="")
            print(my_list[i], end="")
            count += 1  # Increment count if printing succeeds
        print()  # Add newline after all elements are printed
    except IndexError:
        # If we hit an index out of bounds, just add newline and stop
        print()
    return count  # Return the number of elements printed
