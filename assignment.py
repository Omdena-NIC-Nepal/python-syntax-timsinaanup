def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    if number < 10:
        return "Lesser"
    if number == 10:
        return "Equal"

def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    Sum_of_numbers = 0
    for number in range(n+1):
        Sum_of_numbers = Sum_of_numbers + number
    return Sum_of_numbers


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    tuple = (sum(numbers), max(numbers), min(numbers))
    return tuple

def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    list = []
    for name,score in students_dict.items():
        if score > 80:
            list.append(name)
    return list

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    set1 = set(list1)
    set2 = set(list2)

    common_elements = set1 & set2
    return common_elements
    

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    quotient = a / b if b != 0 else "undefined"
    Results = {
        "sum" : a+b,
        "difference" : a-b,
        "product" : a*b,
        "quotient" : quotient
    }
    return Results

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    Results = {
        'and' : x and y,
        'or' : x or y,
        'not_x' : not x
    }
    return Results 

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    Results = {
        'and' : a & b,
        'or' : a | b,
        'xor' : a ^ b
    }
    return Results