
from exercise2.e2prob8 import gpt_even_odd_palindrome
from tests.test_p8 import check

try:
    check(gpt_even_odd_palindrome)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")