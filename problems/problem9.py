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

# Self-planning prompt: Before writing any code, create a clear plan for how to solve the following problem, then implement it.
# 1) Write step-by-step plan describing how you will solve the problem (hint: break down into smaller steps based on what the end goal requirements are)
# 2) Implement the solution in Python as according to the plan.
# 3) Output only the final, working code.
# *copy and paste problem description from above*

def gpt_get_closest_vowel_a(word):
    """Find the closest vowel between two consonants from the right side of the word."""
    vowels = "aeiouAEIOU"
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i-1] not in vowels and word[i+1] not in vowels:
            return word[i]
    return ""

def claude_get_closest_vowel_a(word):
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
    vowels = "aeiouAEIOU"
    
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    
    return ""

# CoT Prompt: Think step by step before coding:
# 1. Understand the task: find the rightmost vowel in the word that is between two consonants. Ignore vowels at the beginning or end.
# 2. Define the set of vowels (both uppercase and lowercase).
# 3. Iterate through the word from right to left, skipping the first and last letters.
# 4. For each character:
#    - Check if it is a vowel.
#    - Check if both neighbors are consonants.
#    - If yes, return that vowel immediately.
# 5. If no such vowel is found, return an empty string.
# 6. Test mentally:
#    - "yogurt" → "u"
#    - "FULL" → "U"
#    - "quick" → ""
#    - "ab" → ""

# Now write the final correct code only.


def gpt_get_closest_vowel_b(word):
    vowels = set("aeiouAEIOU")
    n = len(word)
    if n < 3:
        return ""
    for i in range(n - 2, 0, -1):
        ch = word[i]
        if ch in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return ch
    return ""

def claude_get_closest_vowel_b(word):
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

