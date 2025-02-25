#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize result as None
    try:
        result = a / b  # Perform division
    except ZeroDivisionError:
        # Handle division by zero, keep result as None
        pass
    finally:
        # Always print the result (or None) here
        print("Inside result: {}".format(result))
    return result  # Return the division result or None
