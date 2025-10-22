import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem9 import gpt_get_closest_vowel_a, claude_get_closest_vowel_a, gpt_get_closest_vowel_b, claude_get_closest_vowel_b
from tests.test_p9 import check

# Self-planning
try:
    check(gpt_get_closest_vowel_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-planning
try:
    check(claude_get_closest_vowel_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# CoT
try:
    check(gpt_get_closest_vowel_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# CoT
try:
    check(claude_get_closest_vowel_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")