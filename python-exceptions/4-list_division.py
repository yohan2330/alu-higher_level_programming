#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []  # New list to store division results
    for i in range(list_length):  # Iterate up to list_length
        div_result = 0  # Default result is 0 for invalid cases
        try:
            a = my_list_1[i]  # Access element from first list
            b = my_list_2[i]  # Access element from second list
            # Check if elements are numeric (int or float) by attempting division
            div_result = a / b
        except (TypeError, ValueError):
            print("wrong type")  # Non-numeric types
        except ZeroDivisionError:
            print("division by 0")  # Division by zero
        except IndexError:
            print("out of range")  # List too short
        finally:
            result.append(div_result)  # Add result (division or 0) to list
    return result  # Return the new list
