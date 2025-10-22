import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from problems.problem6 import gpt_count_upper_a, claude_count_upper_a, gpt_count_upper_b, claude_count_upper_b
from tests.test_p6 import check

# Stepwise CoT
try:
    check(gpt_count_upper_a)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Stepwise CoT
try:
    check(claude_count_upper_a)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")
    
# Self-debugging
try:
    check(gpt_count_upper_b)
    print("GPT solution: pass")
except AssertionError:
    print("GPT solution: fail")

# Self-debugging
try:
    check(claude_count_upper_b)
    print("Claude solution: pass")
except AssertionError:
    print("Claude solution: fail")