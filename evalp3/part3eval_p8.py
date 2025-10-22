import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p8 import p3_gpt_even_odd_palindrome, p3_claude_even_odd_palindrome
from tests.test_p8 import check

try:
    check(p3_gpt_even_odd_palindrome)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_even_odd_palindrome)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    