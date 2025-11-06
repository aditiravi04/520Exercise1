# # Problem Descripion

# def even_odd_palindrome(n):
#     """
#     Given a positive integer n, return a tuple that has the number of even and odd
#     integer palindromes that fall within the range(1, n), inclusive.

#     Example 1:

#     Input: 3
#     Output: (1, 2)
#     Explanation:
#     Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

#     Example 2:

#     Input: 12
#     Output: (4, 6)
#     Explanation:
#     Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

#     Note:
#     1. 1 <= n <= 10^3
#     2. returned tuple has the number of even and odd integer palindromes respectively.
#     """
#     return

# CoT Prompt: Think step by step before coding:
# 1. Understand the task: count palindromic numbers from 1 to n, separately for even and odd numbers.
# 2. For each number in the range 1 to n:
#    - Convert it to a string and check if it reads the same forwards and backwards.
#    - If it is a palindrome, check if it is even or odd.
# 3. Keep two counters: one for even palindromes, one for odd palindromes.
# 4. Return the counts as a tuple: (even_count, odd_count).
# 5. Test mentally:
#    - n = 3 → palindromes: 1, 2, 3 → (1, 2)
#    - n = 12 → palindromes: 1-9, 11 → (4, 6)

# Now write the final correct code only.


def gpt_even_odd_palindrome_a(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    
    
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:  # check if palindrome
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
    return (even_count, odd_count)


def claude_even_odd_palindrome_a(n):
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
    
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)

# # Self-debugging prompt: You are a Python expert. Follow these steps carefully:
# 1. Read the following problem and write an initial implementation.
# 2. Mentally test your code on the provided example(s).
# 3. If your code might fail or be incomplete, correct it.
# 4. Output only your final corrected code
# *copy and paste problem description from above*

def gpt_even_odd_palindrome_b(n: int):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    if not isinstance(n, int):
        return -1
    if n < 1:
        return (0, 0)
    even = 0
    odd = 0
    for i in range(1, n + 1):
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd +=1
    return (even, odd)

def claude_even_odd_palindrome_b(n):
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.
    """
    
    even_count = 0
    odd_count = 0
    
    for i in range(1, n + 1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
    
    return (even_count, odd_count)

