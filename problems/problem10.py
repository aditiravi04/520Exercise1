# Problem Descripion

# def cycpattern_check(a , b):
#     """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
#     cycpattern_check("abcd","abd") => False
#     cycpattern_check("hello","ell") => True
#     cycpattern_check("whassup","psus") => False
#     cycpattern_check("abab","baa") => True
#     cycpattern_check("efef","eeff") => False
#     cycpattern_check("himenss","simen") => True

#     """
#     return
    

# CoT Prompt: Think step by step before coding:
# 1. Understand the task: check if the second word `b` or any of its cyclic rotations appears as a substring in the first word `a`.
# 2. Generate all rotations of `b`:
#    - For each rotation, move the first character to the end repeatedly.
# 3. For each rotation, check if it is a substring of `a`.
# 4. If any rotation is found in `a`, return True. Otherwise, return False.
# 5. Test mentally:
#    - "abcd", "abd" → False
#    - "hello", "ell" → True
#    - "abab", "baa" → True

# Now write the final correct code only.


def gpt_cycpattern_check_a(a, b):
    """Return True if b or any cyclic rotation of b is a substring of a."""
    if not b or len(b) > len(a):
        return False
    n = len(b)
    for i in range(n):
        rot = b[i:] + b[:i]
        if rot in a:
            return True
    return False


def claude_cycpattern_check_a(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False

# # Self-debugging prompt: You are a Python expert. Follow these steps carefully:
# 1. Read the following problem and write an initial implementation.
# 2. Mentally test your code on the provided example(s).
# 3. If your code might fail or be incomplete, correct it.
# 4. Output only your final corrected code
# *copy and paste problem description from above*

def gpt_cycpattern_check_b(a, b):
    """Return True if b or any cyclic rotation of b is a substring of a."""
    if not b or len(b) > len(a):
        return False
    n = len(b)
    for i in range(n):
        rot = b[i:] + b[:i]
        if rot in a:
            return True
    return False

def claude_cycpattern_check_b(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True
    """
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False

# --------------------------------------------------PART 2-------------------------------------------------- #

# --------------------------------------------------GPT------------------------------------------------------#

# Self-planning prompt: Think clearly about what the goal is. Consider what the input is and what the expected output is. Break it down into 
# sequential steps and try one more time. Consider the examples to guide you but also consider other edge case scenarios on what your outputs should look like in different cases. 

def gpt_cycpattern_check_try2(a, b):
    """Return True if b or any cyclic rotation of b is a substring of a."""
    if not b or len(b) > len(a):
        return False
    
    n = len(b)
    for i in range(n):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False

# Self-debug prompt: Still failing. Make sure that if both strings are equal or b is empty, it is automatically a match. Other than that, you need to essentially check each rotation of b. Use these hints to inspect where you are going wrong. Correct and debug the solution. Output a correct solution.

def gpt_cycpattern_check_try3(a, b):
    """Return True if b or any of its cyclic rotations is a substring of a."""
    # If both strings are equal or b is empty, it's automatically a match
    if a == b or not b:
        return True
    
    # Check each rotation of b
    length = len(b)
    for j in range(length):
        rotated = b[j:] + b[:j]
        if rotated in a:
            return True
    
    return False


#---------------------------------------------------CLAUDE------------------------------------------------------------#


# Self-planning prompt: Think clearly about what the goal is. Consider what the input is and what the expected output is. Break it down into 
# sequential steps and try one more time. Consider the examples to guide you but also think of other edge-case scenarios on what your outputs should look like in different cases. 

def claude_cycpattern_check_try2(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Handle edge cases
    if not a or not b:
        return False
    if len(b) > len(a):
        return False
    
    # Check all rotations of b
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False

# Self-debug prompt: Still failing. Make sure that if both strings are equal or b is empty, it is automatically a match. Other than that, you need to essentially check each rotation of b. Use these hints to inspect where you are going wrong. Correct and debug the solution. Output a correct solution.

def claude_cycpattern_check_try3(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
    # Handle edge cases
    if a == b:
        return True
    if not b:
        return True
    if len(b) > len(a):
        return False
    
    # Check all rotations of b
    for i in range(len(b)):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False