#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Tracks number of integers printed
    try:
        for i in range(x):  # Loop through x elements
            try:
                # Attempt to print as integer
                print("{:d}".format(my_list[i]), end="")
                count += 1  # Increment if successful (means it’s an integer)
            except (ValueError, TypeError):
                # Silently skip non-integers
                continue
        print()  # Newline after all elements
    except IndexError:
        # Handle case where x exceeds list size
        print()  # Still add newline before exception propagates
        raise  # Let the IndexError bubble up as expected
    return count  # Return number of integers printed
