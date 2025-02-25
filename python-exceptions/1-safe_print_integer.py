#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Attempt to format and print value as an integer
        print("{:d}".format(value))
        return True  # Return True if successful
    except (ValueError, TypeError):
        # Catch ValueError (non-integer) or TypeError (incompatible type)
        return False  # Return False if it fails
