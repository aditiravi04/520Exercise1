import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from part3.part3_p9 import p3_gpt_get_closest_vowel, p3_claude_get_closest_vowel
from tests.test_p9 import check

try:
    check(p3_gpt_get_closest_vowel)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

try:
    check(p3_claude_get_closest_vowel)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
    