# Problem Descripion

def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that returns True if `b` or any rotation of `b` appears as a substring in `a`.  
#    Handle edge cases: if `not b` or `a == b`, return True.

# 2. Self-Test: Mentally test on:
#    - cycpattern_check("abcd","abd") → False  
#    - cycpattern_check("hello","ell") → True  
#    - cycpattern_check("whassup","psus") → False  
#    - cycpattern_check("abab","baa") → True  
#    - cycpattern_check("efef","eeff") → False  
#    - cycpattern_check("himenss","simen") → True  
#    - cycpattern_check("","") → True  
#    - cycpattern_check("abc","") → True  
#    - cycpattern_check("abc","abc") → True  

# 3. Analyze: If any test fails, check rotation logic (`b` in `b+b` trick), substring detection, and edge case handling.

# 4. Refine: Adjust until all tests produce expected outputs.

# 5. Verify: Re-run the tests mentally to confirm correctness.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_cycpattern_check(a, b):
    if not b or a == b:
        return True
    for i in range(len(b)):
        rotated = b[i:] + b[:i]
        if rotated in a:
            return True
    return False

def p3_claude_cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Handle edge cases
    if a == b or not b:
        return True
    
    # Check all rotations of b
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False