# Problem Descripion

def multiply(a, b):
    """Complete the function that takes two integers and returns
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that multiplies the unit digits (last digits) of two integers.

# 2. Self-Test: Mentally test it on:
#    - multiply(148, 412) → 16  
#    - multiply(19, 28) → 72  
#    - multiply(2020, 1851) → 0  
#    - multiply(14, -15) → 20  
#    - multiply(-7, -8) → 56  

# 3. Analyze: If any test fails, identify why (e.g., incorrect handling of negative numbers or extraction of unit digits).

# 4. Refine: Correct the code to consistently get the absolute unit digits and return their product.

# 5. Verify: Re-run the tests mentally to ensure all outputs are correct.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_multiply(a, b):
    x = abs(a) % 10
    y = abs(b) % 10
    return x * y

def p3_claude_multiply(a, b):
    """Complete the function that takes two integers and returns
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    return (abs(a) % 10) * (abs(b) % 10)
