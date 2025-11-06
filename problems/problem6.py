# # Problem Descripion

# def count_upper(s):
#     """
#     Given a string s, count the number of uppercase vowels in even indices.

#     For example:
#     count_upper('aBCdEf') returns 1
#     count_upper('abcdefg') returns 0
#     count_upper('dBBE') returns 0
#     """
#     return

# CoT prompt: 
# 1. Identify what to count — uppercase vowels (A, E, I, O, U) that appear at even indices in the string.
# 2. Plan: loop through the string using indices; for each even index, check if the character is an uppercase vowel.
# 3. Keep a counter and increment it when the condition is met.
# 4. Return the counter at the end.
# 5. Test mentally on examples like 'aBCdEf' → 1, 'abcdefg' → 0, 'dBBE' → 0.
# Now write the final correct code only.
# *copy and paste problem description from above*

def gpt_count_upper_a(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    """
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for i, c in enumerate(s) if i % 2 == 0 and c in vowels)

def claude_count_upper_a(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in 'AEIOU':
            count += 1
    return count

# # Self-debugging prompt: You are a Python expert. Follow these steps carefully:
# 1. Read the following problem and write an initial implementation.
# 2. Mentally test your code on the provided example(s).
# 3. If your code might fail or be incomplete, correct it.
# 4. Output only your final corrected code
# *copy and paste problem description from above*

def gpt_count_upper_b(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    vowels = {"A", "E", "I", "O", "U"}
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in vowels:
            count += 1
    return count

def claude_count_upper_b(s): 
    """ 
    Given a string s, count the number of uppercase vowels in even indices. 
 
    For example: 
    count_upper('aBCdEf') returns 1 
    count_upper('abcdefg') returns 0 
    count_upper('dBBE') returns 0 
    """ 
    uppercase_vowels = 'AEIOU'
    count = 0
    for i in range(0, len(s), 2):
        if s[i] in uppercase_vowels:
            count += 1
    return count
