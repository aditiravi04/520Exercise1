# Problem Descripion

def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between
    two consonants from the right side of the word (case sensitive).

    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition.

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that scans the word from right to left and returns the first vowel that is between two consonants (not at the beginning or end). If none exist, return an empty string.

# 2. Self-Test: Mentally test on:
#    - get_closest_vowel("yogurt") → "u"  
#    - get_closest_vowel("FULL") → "U"  
#    - get_closest_vowel("quick") → ""  
#    - get_closest_vowel("ab") → ""  
#    - get_closest_vowel("strength") → "e"  
#    - get_closest_vowel("APPLE") → ""  
#    - get_closest_vowel("planet") → "a"  

# 3. Analyze: If any test fails, verify consonant detection, boundary handling, and right-to-left traversal logic.

# 4. Refine: Fix the implementation to correctly identify and return the vowel according to the given rules.

# 5. Verify: Re-run the same tests mentally to ensure all expected outputs are correct.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_get_closest_vowel(word):
    vowels = "AEIOUaeiou"
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""

def p3_claude_get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive). 
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't 
    find any vowel met the above condition. You may assume that the given string contains English letter only. 
    Example: 
    get_closest_vowel("yogurt") ==> "u" 
    get_closest_vowel("FULL") ==> "U" 
    get_closest_vowel("quick") ==> "" 
    get_closest_vowel("ab") ==> "" 
    """ 
    vowels = "aeiouAEIOU"
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    
    return ""