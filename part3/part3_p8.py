# Problem Descripion

def even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    Input: 3
    Output: (1, 2)
    Explanation:
    Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    Input: 12
    Output: (4, 6)
    Explanation:
    Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
    1. 1 <= n <= 10^3
    2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    return

# Iterative-Refinement Process (do all of this internally):

# 1. Draft: Write an initial version of the function that counts all integer palindromes between 1 and n (inclusive) and returns a tuple (even_count, odd_count).

# 2. Self-Test: Mentally test on:
#    - even_odd_palindrome(3) → (1, 2)  
#    - even_odd_palindrome(12) → (4, 6)  
#    - even_odd_palindrome(1) → (0, 1)  
#    - even_odd_palindrome(22) → (5, 7)  

# 3. Analyze: If any test fails, check palindrome detection, range boundaries, and even/odd counting.

# 4. Refine: Adjust implementation logic until all expected outputs are correct.

# 5. Verify: Re-run tests mentally to confirm.

# 6. Output: Print only the final, corrected function code — no explanations.

def p3_gpt_even_odd_palindrome(n):
    even = odd = 0
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return (even, odd)

def p3_claude_even_odd_palindrome(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    Input: 3
    Output: (1, 2)
    Explanation:
    Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    Input: 12
    Output: (4, 6)
    Explanation:
    Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
    1. 1 <= n <= 10^3
    2. returned tuple has the number of even and odd integer palindromes respectively.
    """
    
    even_count = 0
    odd_count = 0

    def is_palindrome(num):
        s = str(num)
        return s == s[::-1]

    for i in range(1, n + 1):
        if is_palindrome(i):
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)