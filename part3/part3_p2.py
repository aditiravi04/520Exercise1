# Problem Descripion

from typing import List
def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance. Your task is to detect if at any point the balance of account fallls below zero, and at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    return

# Iterative-refinement prompt: Do all this internally.
# 1. Draft: Write an initial version of the function that checks if the running balance ever drops below zero.

# 2. Self-Test: Mentally test it on:
#    - below_zero([1, 2, 3]) → False  
#    - below_zero([1, 2, -4, 5]) → True  
#    - below_zero([-1]) → True  
#    - below_zero([0, 0, 0]) → False  
#    - below_zero([10, -5, -5]) → False  

# 3. Analyze: If any test fails, identify why (e.g., incorrect loop logic or early return condition).

# 4. Refine: Adjust the code to correctly track the balance and return True as soon as it goes below zero.

# 5. Verify: Re-run the tests mentally to ensure all expected outputs are correct.

# 6. Output: Print only the final, corrected function code — no explanations.


def p3_gpt_below_zero(operations: List[int]) -> bool:
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False

from typing import List

def p3_claude_below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with zero balance. Your task is to detect if at any point the balance of account fallls below zero, and at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False