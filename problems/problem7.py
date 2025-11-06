# # Problem Descripion

# def is_bored(S):
#     """
#     You'll be given a string of words, and your task is to count the number
#     of boredoms. A boredom is a sentence that starts with the word "I".
#     Sentences are delimited by '.', '?' or '!'.

#     For example:
#     >>> is_bored("Hello world")
#     0
#     >>> is_bored("The sky is blue. The sun is shining. I love this weather")
#     1
#     """
#     return

# Self-repair prompt: You are an expert Python programmer. 
# Follow these steps carefully:
# 1. Write your initial implementation of the function.
# 2. Analyze your code and identify possible errors or edge cases that might fail.
# 3. Repair your implementation to fix those issues.
# 4. Output only the final, correct version of your code.
# *copy and paste problem description from above*

import re

def gpt_is_bored_a(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    sentences = re.split(r'[.?!]', S)
    return sum(1 for sentence in sentences if sentence.strip().startswith("I"))

def claude_is_bored_a(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith('I ') or sentence == 'I':
            count += 1
    return count

# CoT Prompt: Think step by step before coding:
# 1. Understand the task: count how many sentences start with the word "I".
# 2. Sentences are split by '.', '?', or '!'. Use this to separate them.
# 3. For each sentence:
#    - Strip leading/trailing spaces.
#    - Check if it starts with "I " or is exactly "I".
# 4. Keep a counter for such sentences.
# 5. Return the counter at the end.
# 6. Test mentally: 
#    - "Hello world" → 0
#    - "The sky is blue. The sun is shining. I love this weather" → 1

# Now write the final correct code only.


import re

def gpt_is_bored_b(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    parts = re.split(r'[.?!]', S)
    count = 0
    for p in parts:
        p = p.strip()
        if p == "I" or p.startswith("I "):
            count += 1
    return count

def claude_is_bored_b(S): 
    """ 
    You'll be given a string of words, and your task is to count the number 
    of boredoms. A boredom is a sentence that starts with the word "I". 
    Sentences are delimited by '.', '?' or '!'. 
 
    For example: 
    >>> is_bored("Hello world") 
    0 
    >>> is_bored("The sky is blue. The sun is shining. I love this weather") 
    1 
    """ 
    import re
    sentences = re.split(r'[.!?]', S)
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith("I ") or sentence == "I":
            count += 1
    return count

# --------------------------------------------------PART 2-------------------------------------------------- #

# --------------------------------------------------GPT------------------------------------------------------#

# Self-repair prompt: Think clearly about what the goal is. Make sure you do not get confused with sentences that have I in the middle. We only want the sentences that start with 'I'. Remember how sentences are delimited by. Try again.

import re

def gpt_is_bored_try2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    """
    # Split string into sentences including delimiter to correctly identify starts
    sentences = re.split(r'(?<=[.?!])', S)
    count = 0
    for sentence in sentences:
        stripped = sentence.strip()
        if stripped and stripped[0] == 'I' and (len(stripped) == 1 or stripped[1] == ' '):
            count += 1
    return count

# Self-debug prompt: Still failing. These are the tests that are failing, your current outputs, and their expected outputs: *insert copy and paste of tests failing with expected responses*. Use this to inspect where you are going wrong. Correct and debug the solution. Output a correct solution.

import re

def gpt_is_bored_try3(S):
    """
    Count the number of sentences that start with the word 'I'.
    Sentences are delimited by '.', '?' or '!'.
    """
    # Split text into sentences by punctuation
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        words = sentence.strip().split()
        if words and words[0] == "I":
            count += 1
    return count

# Self-debug prompt: Still failing. Consider using built in python functions. Consider normalizing to make it easier for you to understand what cases to consider. Take a look at the problem instructions and failing test cases. Make a list, and try to debug it problem by problem. Output a correct solution.

def gpt_is_bored_try4(S):
    """
    Count the number of sentences that start with the word 'I'.
    Sentences are delimited by '.', '?' or '!'.
    """
    # Normalize all sentence delimiters to '.'
    normalized = S.replace('?', '.').replace('!', '.')
    # Split into sentences and strip whitespace
    sentences = [s.strip() for s in normalized.split('.') if s.strip()]
    # Count sentences that start with 'I '
    return sum(s.startswith('I ') for s in sentences)

#---------------------------------------------------CLAUDE------------------------------------------------------------#

# Self-repair prompt: Think clearly about what the goal is. Make sure you do not get confused with sentences that have I in the middle. We only want the sentences that start with 'I'. Remember how sentences are delimited by. Try again.

def claude_is_bored_try2(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    sentences = re.split(r'[.?!]', S)
    count = 0
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence.startswith('I ') or sentence == 'I':
            count += 1
    return count

# Self-debug prompt: Still failing. These are the tests that are failing, your current outputs, and their expected outputs: *insert copy and paste of tests failing with expected responses*. Use this to inspect where you are going wrong. Correct and debug the solution. Output a correct solution.

def claude_is_bored_try3(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.

    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    import re
    # Split by delimiters and filter empty strings
    sentences = [s.strip() for s in re.split(r'[.?!]', S) if s.strip()]
    # Count how many sentences start with 'I '
    count = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            count += 1
    return count