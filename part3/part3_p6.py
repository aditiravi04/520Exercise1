# Problem Descripion

def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.

    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that counts uppercase vowels ('A', 'E', 'I', 'O', 'U') appearing at even indices in the string.

# 2. Self-Test: Mentally test on:
#    - count_upper('aBCdEf') → 1  
#    - count_upper('abcdefg') → 0  
#    - count_upper('dBBE') → 0  
#    - count_upper('AeiOu') → 1  

# 3. Analyze: If any test fails, identify issues (e.g., index logic, case sensitivity, or vowel set).

# 4. Refine: Fix index checking and vowel detection until all tests yield correct results.

# 5. Verify: Re-run tests mentally to confirm correctness.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_count_upper(s):
    vowels = {'A', 'E', 'I', 'O', 'U'}
    return sum(1 for i, ch in enumerate(s) if i % 2 == 0 and ch in vowels)

def p3_claude_count_upper(s):
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