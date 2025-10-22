# Problem Descripion

def is_bored(S):
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
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that counts how many sentences start with the word "I". Sentences are split by '.', '?', or '!'.

# 2. Self-Test: Mentally test on:
#    - is_bored("Hello world") → 0  
#    - is_bored("The sky is blue. The sun is shining. I love this weather") → 1  
#    - is_bored("I am here! I am bored.") → 2  
#    - is_bored("This is fine. i'm okay.") → 0  

# 3. Analyze: If any test fails, check sentence-splitting, trimming spaces, and ensuring exact match for sentences starting with "I".

# 4. Refine: Adjust logic until all tests pass.

# 5. Verify: Re-run all tests mentally.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_is_bored(S):
    import re
    sentences = re.split(r'[.?!]', S)
    return sum(1 for s in sentences if s.strip().startswith('I '))

def p3_claude_is_bored(S):
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
        stripped = sentence.strip()
        if stripped.startswith('I ') or stripped == 'I':
            count += 1
    return count