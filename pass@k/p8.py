import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem8 import gpt_even_odd_palindrome_a, claude_even_odd_palindrome_a, gpt_even_odd_palindrome_b, claude_even_odd_palindrome_b
from tests.test_p8 import check

# Stepwise-CoT
try:
    check(gpt_even_odd_palindrome_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Stepwise-CoT
try:
    check(claude_even_odd_palindrome_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# Self-debugging
try:
    check(gpt_even_odd_palindrome_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_even_odd_palindrome_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")