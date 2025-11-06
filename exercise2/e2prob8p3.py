# GPT's solution to self-debugging prompt: 

def gpt_even_odd_palindrome(n: int):
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
    for i in range(1, n): #Excluded the upper bound - a pretty common/probably mistake
        s = str(i)
        if s == s[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd +=1
    return (even, odd)
