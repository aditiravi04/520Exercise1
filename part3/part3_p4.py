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

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that checks if all inputs are integers and if one equals the sum of the other two.

# 2. Self-Test: Mentally test it on:
#    - any_int(5, 2, 7) → True  
#    - any_int(3, 2, 2) → False  
#    - any_int(3, -2, 1) → True  
#    - any_int(3.6, -2.2, 2) → False  
#    - any_int(0, 0, 0) → True  

# 3. Analyze: If any test fails, identify why (e.g., missing integer type check, incorrect equality logic, or rounding issue).

# 4. Refine: Fix the code to correctly enforce integer type checking and verify all possible sum combinations.

# 5. Verify: Re-run the tests mentally to ensure all results match the expected outputs.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_any_int(x, y, z):
    if not all(isinstance(i, int) for i in [x, y, z]):
        return False
    return x == y + z or y == x + z or z == x + y

def p3_claude_any_int(x, y, z):
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