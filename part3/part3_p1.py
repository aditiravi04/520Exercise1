# Problem Descripion

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return

# Iterative-refinement prompt: Do all this internally.
# 1. Draft: Write an initial version of the function.

# 2. Self-Test: Mentally test it on:
#    - truncate_number(3.5) → 0.5  
#    - truncate_number(7.12) → 0.12  
#    - truncate_number(0.99) → 0.99  
#    - truncate_number(5.0) → 0.0  
#    - truncate_number(1234.567) → 0.567  

# 3. Analyze: If any test fails, identify the cause (e.g., rounding or integer conversion errors).
# 4. Refine: Adjust the code to fix the issues.
# 5. Verify: Re-run the tests mentally to ensure all outputs are correct.
# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    import math 
    return number - math.floor(number)

def p3_claude_truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    return number - int(number)

    
    

