# Problem Descripion

# def truncate_number(number: float) -> float:
#     """ Given a positive floating point number, it can be decomposed into
#     and integer part (largest integer smaller than given number) and decimals
#     (leftover part always smaller than 1).

#     Return the decimal part of the number.
#     >>> truncate_number(3.5)
#     0.5
#     """
#     return

# Self-planning prompt: Before writing any code, create a clear plan for how to solve the following problem, then implement it.
# 1) Write step-by-step plan describing how you will solve the problem (hint: break down into smaller steps based on what the end goal requirements are)
# 2) Implement the solution in Python as according to the plan.
# 3) Output only the final, working code.
# *copy and paste problem description from above*

import math

def gpt_truncate_number_a(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return math.modf(number)[0]

def claude_truncate_number_a(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1

# # Self-debugging prompt: You are a Python expert. Follow these steps carefully:
# 1. Read the following problem and write an initial implementation.
# 2. Mentally test your code on the provided example(s).
# 3. If your code might fail or be incomplete, correct it.
# 4. Output only your final corrected code
# *copy and paste problem description from above*

import math

def gpt_truncate_number_b(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - math.floor(number)

def claude_truncate_number_b(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number % 1