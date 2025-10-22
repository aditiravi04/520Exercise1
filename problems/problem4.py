# Problem Descripion

def any_int(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False
    """
    return

# Self-planning prompt: Before writing any code, create a clear plan for how to solve the following problem, then implement it.
# 1) Write step-by-step plan describing how you will solve the problem (hint: break down into smaller steps based on what the end goal requirements are)
# 2) Implement the solution in Python as according to the plan.
# 3) Output only the final, working code.
# *copy and paste problem description from above*


def gpt_any_int_a(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    vals = (x, y, z)
    for v in vals:
        if not (isinstance(v, int) or (isinstance(v, float) and v.is_integer())):
            return False
    a, b, c = (int(x), int(y), int(z))
    return a == b + c or b == a + c or c == a + b


def claude_any_int_a(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False
    """
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return x == y + z or y == x + z or z == x + y

# Self-debugging prompt: You are a Python expert. Follow these steps carefully:
# 1. write an initial implementation for this function.
# 2. Mentally test your code on the examples.
# 3. If your code might fail or be incomplete, correct it.
# 4. Output only your final corrected code
# *copy and paste problem description from above*

def gpt_any_int_b(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    """
    def is_strict_int(n):
        return isinstance(n, int) and not isinstance(n, bool)

    if not (is_strict_int(x) and is_strict_int(y) and is_strict_int(z)):
        return False

    return x == y + z or y == x + z or z == x + y

def claude_any_int_b(x, y, z):
    """
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.

    Examples
    any_int(5, 2, 7) ➞ True

    any_int(3, 2, 2) ➞ False

    any_int(3, -2, 1) ➞ True

    any_int(3.6, -2.2, 2) ➞ False
    """
    if not (isinstance(x, int) and isinstance(y, int) and isinstance(z, int)):
        return False
    return x == y + z or y == x + z or z == x + y
